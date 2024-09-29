from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from user import models


class UserValidateSerializer(serializers.Serializer):
    sername = serializers.CharField(max_length=150)
    password = serializers.CharField()


class UserAuthSerializer(serializers.ModelSerializer):
    pass


class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConfirmCode
        fields = ['email', 'code']
        read_only_fields = ['code']


class UserCreateSerializer(UserValidateSerializer):

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("User already exists")
        return username
