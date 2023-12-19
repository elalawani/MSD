from rest_framework import serializers
from .models import Task
from account.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'patient', 'user', 'completed', 'created_at', 'updated_at']
