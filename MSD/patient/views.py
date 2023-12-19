from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from conversation.models import Conversation
from .filters import PatientFilter
from .serializers import PatientSerializer
from .models import Patient
from .forms import PatientForm
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


pagination = StandardResultsSetPagination()


@api_view(['GET'])
def patient_list_filtered(request):
    user = request.user
    if user.role == 'ST':
        patients = Patient.objects.all().distinct()
    elif user.role == 'DR':
        patients = Patient.objects.filter(doctors=user).distinct()
    elif user.role == 'NR':
        patients = Patient.objects.filter(nurses=user).distinct()
    else:
        raise PermissionDenied("You do not have permission to views patients.")

    filtered = PatientFilter(request.GET, queryset=patients)

    serializer = PatientSerializer(filtered.qs, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def patient_list(request):
    user = request.user
    if user.role == 'ST':
        patients = Patient.objects.all().distinct()
    elif user.role == 'DR':
        patients = Patient.objects.filter(doctors=user).distinct()
    elif user.role == 'NR':
        patients = Patient.objects.filter(nurses=user).distinct()
    else:
        raise PermissionDenied("You do not have permission to views patients.")

    serializer = PatientSerializer(patients, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def patient(request, pk):
    user = request.user
    try:
        patient_info = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist.")

    if user.role == 'ST':
        pass
    elif user.role == 'DR':
        if not Patient.objects.filter(doctors=user, pk=pk).exists():
            raise PermissionDenied("You do not have permission to views patients.")
    elif user.role == 'NR':
        if not Patient.objects.filter(nurses=user, pk=pk).exists():
            raise PermissionDenied("You do not have permission to views patients.")
    else:
        raise PermissionDenied("You do not have permission to views patients.")

    if request.method == 'GET':
        serializer = PatientSerializer(patient_info, context={'request': request})
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_patient(request):
    form = PatientForm(request.data)
    if form.is_valid():
        patient = form.save(commit=False)
        patient.created_by = request.user
        patient.save()

        doctors = form.cleaned_data.get('doctors')
        nurses = form.cleaned_data.get('nurses')

        patient.doctors.set(doctors)
        patient.nurses.set(nurses)

        conversation = Conversation.objects.create(patient=patient)
        # conversation.users.add(*doctors, *nurses)
        for user in list(doctors) + list(nurses):
            conversation.users.add(user)

        patient.save()

        return JsonResponse({'message': 'success'})

    else:
        return JsonResponse({'message': 'error', 'errors': form.errors})


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist.")

    form = PatientForm(request.data, instance=patient)
    if form.is_valid():
        updated_patient = form.save()
        return JsonResponse({'message': 'success', 'patient': PatientSerializer(updated_patient).data})
    else:
        return JsonResponse({'message': 'error', 'errors': form.errors})


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return JsonResponse({'message': 'Patient has been deleted'})
