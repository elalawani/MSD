from rest_framework import serializers

from account.serializers import UserSerializer
from .models import FhirMeasurement, Comments


class FhirMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FhirMeasurement
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'
