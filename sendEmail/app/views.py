from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendEmailSerializers

from mimetypes import guess_type
from os.path import basename
import smtplib
import os

# Create your views here.


class SendMail(APIView):
    def post(self, request):
        serializer = SendEmailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = EmailMultiAlternatives(serializer.data['subject'], serializer.data['message'], 'arpansainiwins@gmail.com', [
                serializer.data['sendTo']])
            print("--------------------",serializer.data['file'])
            
            attachment = open(os.path.join(os.path.realpath('.'), serializer.data['file'].lstrip("/")), 'rb')
            email.attach(serializer.data['file'].lstrip("/media/"), attachment.read())
            email.send()
            

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        