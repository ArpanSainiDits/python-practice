from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer
import random
from django.core.mail import send_mail, EmailMultiAlternatives
# Create your views here.


class registerAPIView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_active = False
            serializer.save()
            user_otp = random.randint(100000, 999999)
            
            email = EmailMultiAlternatives('Confirmation mail.', 'You have successfully registered.', 'arpansainiwins@gmail.com', [
                serializer.data['email']])
            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
