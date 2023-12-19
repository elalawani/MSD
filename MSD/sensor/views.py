from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *


@api_view(['POST'])
def post_heart_rate(request):
    serializer = HeartRateMeasurementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_heart_rate(request, patient_id):
    try:
        measurements = HeartRateMeasurement.objects.filter(patient_id=patient_id)
    except HeartRateMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = HeartRateMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_blood_pressure(request):
    if request.method == 'POST':
        serializer = BloodPressureMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_blood_pressure(request, patient_id):
    try:
        measurements = BloodPressureMeasurement.objects.filter(patient_id=patient_id)
    except BloodPressureMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = BloodPressureMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_blood_glucose(request):
    if request.method == 'POST':
        serializer = BloodGlucoseMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_blood_glucose(request, patient_id):
    try:
        measurements = BloodGlucoseMeasurement.objects.filter(patient_id=patient_id)
    except BloodGlucoseMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = BloodGlucoseMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_respiration_rate(request):
    if request.method == 'POST':
        serializer = RespirationRateMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_respiration_rate(request, patient_id):
    try:
        measurements = RespirationRateMeasurement.objects.filter(patient_id=patient_id)
    except RespirationRateMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = RespirationRateMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_temperature(request):
    if request.method == 'POST':
        serializer = TemperatureMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_temperature(request, patient_id):
    try:
        measurements = TemperatureMeasurement.objects.filter(patient_id=patient_id)
    except TemperatureMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = TemperatureMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_blood_cholesterol(request):
    if request.method == 'POST':
        serializer = BloodCholesterolMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_blood_cholesterol(request, patient_id):
    try:
        measurements = BloodCholesterolMeasurement.objects.filter(patient_id=patient_id)
    except BloodCholesterolMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = BloodCholesterolMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_parkinson(request):
    if request.method == 'POST':
        serializer = ParkinsonsMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_parkinson(request, patient_id):
    try:
        measurements = ParkinsonsMeasurement.objects.filter(patient_id=patient_id)
    except ParkinsonsMeasurement.DoesNotExist:
        raise Http404("measurements does not exist.")
    serializer = ParkinsonsMeasurementSerializer(measurements, many=True)
    return Response(serializer.data)
