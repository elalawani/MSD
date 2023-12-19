from rest_framework import serializers
from .models import Conversation, ConversationMessage

from account.serializers import UserSerializer
from patient.serializers import PatientSerializer


class ConversationMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ['id', 'conversation', 'content', 'created_at_formatted', 'user']


class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    messages = ConversationMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'patient', 'users', 'created_at', 'modified_at', 'messages']


class OnlyConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'patient', 'users', 'created_at']
