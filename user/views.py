from pip._vendor.rich.prompt import Confirm
from rest_framework import status
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from user import models


@api_view(['POST'])
def registration_api_view(request):
    serializer = serializers.UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})


@api_view(['POST'])
def send_confirm_code_api_view(request):
    serializer = serializers.ConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    confirm = serializer.save()
    confirm.generate_code()
    send_mail(
        'YOUR CONFIRMATION CODE',
        f'YOUR CONFIRMATION CODE{confirm.code}',
        'adcvbdc@gmail.com',
        [confirm.email],
        False)
    return Response(
        status=status.HTTP_201_CREATED
    )


@api_view(['post'])
def confirm_email_api_view(request):
    email = request.data.get('email')
    code = request.data.get('code')
    try:
        confirm = Confirm.objects.get(email=email)
        if confirm.code != code:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_200_OK)
    except Confirm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = serializers.UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key}, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
