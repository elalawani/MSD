import uuid

from django.db import models
from account.models import User
from patient.models import Patient


class Measurement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='%(class)s_creator', on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, null=True)
    code = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


class HeartRateMeasurement(Measurement):
    HeartRate = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='bpm')


class BloodPressureMeasurement(Measurement):
    systolic_Pressure = models.FloatField(null=True, blank=True)
    diastolic_Pressure = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mmHg')


class BloodGlucoseMeasurement(Measurement):
    BloodGlucose = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class RespirationRateMeasurement(Measurement):
    RespirationRate = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='breaths per minute')


class TemperatureMeasurement(Measurement):
    Temperature = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='°C')


class BloodCholesterolMeasurement(Measurement):
    BloodCholesterol = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class ParkinsonsMeasurement(Measurement):
    TREMOR_SEVERITY_CHOICES = [
        (1, 'Slight'),
        (2, 'Noticeable'),
        (3, 'Moderate'),
        (4, 'Severe'),
    ]
    tremor_severity = models.IntegerField(choices=TREMOR_SEVERITY_CHOICES)
    gait_speed = models.FloatField()
    daily_assessment = models.IntegerField()
