from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
import json
import requests
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from patient.models import Patient
from .models import FhirMeasurement, Comments
from .serializers import FhirMeasurementSerializer, CommentsSerializer


@api_view(['POST'])
def upload_measurement(request):
    # check if files are exist
    if 'file' not in request.FILES:
        return JsonResponse({"error": "Keine Datei bereitgestellt."}, status=400)

    # read the file
    file = request.FILES['file']
    file_content = file.read().decode('utf-8')
    file.close()

    # check format
    try:
        json_data = json.loads(file_content)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Ungültige JSON-Datei bereitgestellt."}, status=400)

    patient_id = request.POST.get('patient', None)
    if not patient_id:
        return JsonResponse({"error": "Keine Patienten-ID angegeben."}, status=400)

    # Validate using HAPI FHIR Server
    response = requests.post(
        # validation (fhir is the name of the service for the fhir server)
        # see on Docker-compose.yml File
        'http://fhir:8080/fhir/Observation/$validate',
        headers={'Content-Type': 'application/fhir+json'},
        json=json_data,
        timeout=10
    )
    # for debugging and checking the Response
    # print("FHIR server response:", response.text)

    if response.status_code == 200:
        validation_output = response.json()
        if validation_output.get('issue'):
            severity = validation_output['issue'][0].get('severity')
            if severity not in ['information', 'informational']:
                # Handle error
                return JsonResponse({"error": "Ungültige FHIR-Daten!",
                                     "details": validation_output.get('issue')},
                                    status=400)
    else:
        return JsonResponse({"error": "FHIR-Server hat einen Fehler zurückgegeben.", "details": response.text}, status=500)

    status = request.POST.get('status', None)
    movement = request.POST.get('movement', None)
    if not status:
        return JsonResponse({"error": "Kein Status angegeben."}, status=400)

    if not movement:
        return JsonResponse({"error": "Keine Bewegung angegeben."}, status=400)

    initial_data = {
        'data': json_data,
        'patient': patient_id,
        'uploaded_by': request.user.id,
        'status': status,
        'movement': movement

    }
    serializer = FhirMeasurementSerializer(data=initial_data)

    # post into DB
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def get_all_measurements(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise PermissionDenied("Patient existiert nicht")

    measurements = FhirMeasurement.objects.filter(patient=patient)
    serializer = FhirMeasurementSerializer(measurements, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def create_measurement_comment(request):
    serializer = CommentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_measurement_comments(request, patient_id):
    measurements = FhirMeasurement.objects.filter(patient_id=patient_id).values_list('id', flat=True)

    if not measurements.exists():
        return Response({"message": "No measurements found for this patient."}, status=status.HTTP_404_NOT_FOUND)

    comments = Comments.objects.filter(measurement__in=measurements).order_by('-created_at')

    if not comments.exists():
        return Response({"message": "No comments found for the given measurements."}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentsSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
