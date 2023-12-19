from rest_framework import serializers
from .models import *
from account.serializers import UserSerializer


class MeasurementSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Measurement
        fields = ['id', 'created_by', 'created_at', 'status', 'patient', 'code', 'category']


class ParkinsonsMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = ParkinsonsMeasurement
        fields = MeasurementSerializer.Meta.fields + ['tremor_severity', 'gait_speed', 'daily_assessment']


class BloodGlucoseMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = BloodGlucoseMeasurement
        fields = MeasurementSerializer.Meta.fields + ['BloodGlucose', 'unit']


class BloodPressureMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = BloodPressureMeasurement
        fields = MeasurementSerializer.Meta.fields + ['systolic_Pressure', 'diastolic_Pressure', 'unit']


class HeartRateMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = HeartRateMeasurement
        fields = MeasurementSerializer.Meta.fields + ['HeartRate', 'unit']


class RespirationRateMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = RespirationRateMeasurement
        fields = MeasurementSerializer.Meta.fields + ['RespirationRate', 'unit']


class TemperatureMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = TemperatureMeasurement
        fields = MeasurementSerializer.Meta.fields + ['Temperature', 'unit']


class BloodCholesterolMeasurementSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        model = BloodCholesterolMeasurement
        fields = MeasurementSerializer.Meta.fields + ['BloodCholesterol', 'unit']
