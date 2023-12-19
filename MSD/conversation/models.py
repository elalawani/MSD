import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User
from patient.models import Patient


class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='conversation')
    users = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ConversationMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, related_name='message', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)

    def created_at_formatted(self):
        return timesince(self.created_at)

