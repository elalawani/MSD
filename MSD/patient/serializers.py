from rest_framework import serializers

from .models import Patient
from account.serializers import UserSerializer


class PatientSerializer(serializers.ModelSerializer):
    doctors = UserSerializer(many=True, read_only=False)
    nurses = UserSerializer(many=True, read_only=False)

    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'gender', 'street', 'house_number', 'postal_code', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses', 'reason_of_visiting', 'created_by',
                  'created_at', 'full_name', 'age')
