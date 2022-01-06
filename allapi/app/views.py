from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.mail import EmailMultiAlternatives
import random
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from.serializers import UserRegistrationSerializer, otpVerifySerializer, UserLoginSerializer, forgetpasswordSerializer
from.models import otpVerify, User
# Create your views here.


class registerAPIView(APIView):
    def post(self, request):
        user_otp = random.randint(100000, 999999)
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            obj = User.objects.get(email=serializer.data['email'])
            user_obj = otpVerify()
            user_obj.User = obj
            user_obj.registerotp = user_otp
            user_obj.save()

            email = EmailMultiAlternatives('Confirmation mail.', f'Your verification OTP is {user_otp}', 'arpansainiwins@gmail.com', [
                serializer.data['email']])

            email.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class otpVerifyAPIView(APIView):

    def post(self, request):

        serializer = otpVerifySerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()

            user_obj = otpVerify.objects.get(
                User__email=serializer.data['email'])

            if serializer.data['registerotp'] == user_obj.registerotp:

                print("******  otp is matched  *******")

                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'otp is matched',
                    'user': serializer.data
                }
                return Response(response, tiv(serializer.data['email']))
            else:
                print("***** otp did not match *******")
                status_code = status.HTTP_400_BAD_REQUEST

                response = {
                    'success': False,
                    'statusCode': status_code,
                    'message': 'otp did not match',
                    'user': serializer.data
                }
                return Response(response)


def tiv(email):

    pf = User.objects.get(email=email)
    # for item in pf:
    pf.is_active = True
    pf.email_verify = True
    pf.save()


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                # 'authenticatedUser': {
                #     'email': serializer.data['email'],

                # }
            }

            return Response(response, status=status_code)


class forgetPasswordView(APIView):
    def post(self, request):

        user_otp = random.randint(100000, 999999)

        serializer = forgetpasswordSerializer(data=request.data)
        alldatas = {}
        if serializer.is_valid(raise_exception=True):

            mname = serializer.save()

            obj = User.objects.get(email=serializer.data['email'])
            user_obj = otpVerify.objects.get(User=obj)
            user_obj.registerotp = user_otp
            user_obj.save()

            email = EmailMultiAlternatives('Confirmation mail.', f'verification otp is {user_otp}', 'arpansainiwins@gmail.com', [
                serializer.data['email']])
            email.send()

            pf = User.objects.get(email=serializer.data['email'])

            pf.is_active = False
            pf.email_verify = False
            pf.save()

            alldatas['data'] = 'successfully registered'
            print(alldatas)

            return Response(alldatas)
        return Response('failed retry after some time')


class otpVerifyView2(APIView):

    def post(self, request):

        serializer = otpVerifySerializer(data=request.data)
        if serializer.is_valid():

            # serializer.save()

            # user_obj = User.objects.get(email=serializer.data['email'])

            user_obj = otpVerify.objects.get(
                User__email=serializer.data['email'])

            if serializer.data['registerotp'] == user_obj.registerotp:

                print("******  otp is matched  *******")

                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'otp is matched',
                    'user': serializer.data
                }
                return Response(response, tiv(serializer.data['email']))
            else:
                print("***** otp did not match *******")
                status_code = status.HTTP_400_BAD_REQUEST

                response = {
                    'success': False,
                    'statusCode': status_code,
                    'message': 'otp did not match',
                    'user': serializer.data
                }
                return Response(response)
