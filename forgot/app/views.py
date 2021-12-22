from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
import random
from django.core.mail import message, send_mail, EmailMultiAlternatives

class register(APIView):
    def post(self, request):


        serializer = registerSerializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            registerdata = serializer.save()
            data['response'] ='successfully registered'
            data['username'] = registerdata.username
            data['email'] = registerdata.email
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self, request):


        serializer = loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            auth.login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response('invalid username and password try again')


class resetpassword(APIView):
    def post(self, request):
        user_otp = random.randint(100000, 999999)

        serializer = resetpasswordSerializer(data=request.data)
        alldatas = {}
        if serializer.is_valid(raise_exception=True):
            mname = serializer.save()
            
            email = EmailMultiAlternatives('Confirmation mail.', f'verification otp is {user_otp}', 'arpansainiwins@gmail.com', [
                serializer.data['email']])
            email.send()
            
            alldatas['data'] ='successfully registered'
            print(alldatas)
            return Response(alldatas)
        return Response('failed retry after some time')
    
    
class logout(APIView):
    def get(self, request):


        request.user.auth_token.delete()
        auth.logout(request)
        return Response("successfully deleted")
