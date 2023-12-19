from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound
from .models import BarthelIndex
from .serializers import BarthelIndexSerializer
from patient.models import Patient


@api_view(['POST'])
def create_barthel_index(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise PermissionDenied("Patient does not exist")

    serializer = BarthelIndexSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user, patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_barthel_indexes(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise PermissionDenied("Patient does not exist")

    barthel_indexes = BarthelIndex.objects.filter(patient=patient)
    serializer = BarthelIndexSerializer(barthel_indexes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def barthel_index_detail(request, patient_id, barthel_index_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
        barthel_index = BarthelIndex.objects.get(pk=barthel_index_id, patient=patient)
    except Patient.DoesNotExist:
        raise PermissionDenied("Patient does not exist")
    except BarthelIndex.DoesNotExist:
        raise NotFound("BarthelIndex does not exist")

    if request.method == 'GET':
        serializer = BarthelIndexSerializer(barthel_index)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BarthelIndexSerializer(barthel_index, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        barthel_index.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# send all CHOICES to the Frontend
@api_view(['GET'])
def barthel_index_choices(request):
    return Response({
        'barthel_food': BarthelIndex.FOOD_CHOICES,
        'barthel_wash': BarthelIndex.WASH_CHOICES,
        'barthel_shower': BarthelIndex.SHOWER_CHOICES,
        'barthel_dress': BarthelIndex.DRESS_CHOICES,
        'barthel_stool': BarthelIndex.STOOL_CHOICES,
        'barthel_urin': BarthelIndex.URINE_CHOICES,
        'barthel_wc': BarthelIndex.WC_USE_CHOICES,
        'barthel_transf': BarthelIndex.TRANSFERS_CHOICES,
        'barthel_walk': BarthelIndex.WALK_CHOICES,
        'barthel_staris': BarthelIndex.STAIRS_CHOICES,
    })
