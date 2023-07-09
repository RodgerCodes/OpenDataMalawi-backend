from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)


class VerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VerificationCodes
        fields = '__all__'
