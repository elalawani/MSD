import uuid

from django.db import models
from account.models import User
from patient.models import Patient


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='todo_for_patient', on_delete=models.CASCADE,
                                blank=True, null=True)
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
