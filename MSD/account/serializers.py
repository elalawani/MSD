from rest_framework import serializers

from .models import User


class UserSerializerProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'avatar', 'role', 'gender', 'street',
                  'nr', 'PLZ', 'city')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserAddressUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('street', 'nr', 'PLZ', 'city')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'id')
