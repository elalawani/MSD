from django.db import models
from django.db.models import JSONField
from account.models import User
from patient.models import Patient


class FhirMeasurement(models.Model):
    data = JSONField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='measures')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_measurement')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    movement = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])


class Comments(models.Model):
    measurement = models.ForeignKey(FhirMeasurement, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
