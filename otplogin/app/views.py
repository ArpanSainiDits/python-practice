from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserRegistrationSerializer, otpVerifySerializer, UserLoginSerializer, resetpasswordSerializer
import random
from django.core.mail import message, send_mail, EmailMultiAlternatives
import jwt
from .models import User
# from rest_framework_jwt.utils import jwt_decode_handler
# Create your views here.


val = None


class registerAPIView(APIView):

    def post(self, request):

        user_otp = random.randint(100000, 999999)
        global val

        def val():
            return user_otp
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.is_active = False
            serializer.save()

            print("--------------------->>>>>>>>>>.", user_otp)
            print("000000000000000", serializer.data)

            email = EmailMultiAlternatives('Confirmation mail.', f'Your verification OTP is {user_otp}', 'arpansainiwins@gmail.com', [
                serializer.data['email']])

            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class otpVerifyAPIView(APIView):

    def post(self, request):
        ok = val()

        serializer = otpVerifySerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            if serializer.data['otp'] == ok:

                print("******  otp is matched  *******")

                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'otp is matched',
                    'user': serializer.data
                }
                return Response(response, tiv())
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

        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def tiv():

    pf = User.objects.filter()
    for item in pf:
        item.is_active = True
        item.save()


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
                'authenticatedUser': {
                    'email': serializer.data['email'],

                }
            }

            return Response(response, status=status_code)


# class ChangePasswordView(APIView):
    # serializer_class = ChangePasswordSerializer
    # permission_classes = (AllowAny, )

    # def post(self, request):
        # user_otp = random.randint(100000, 999999)
        # serializer = ChangePasswordSerializer(data=request.data)
        # # serializer = self.serializer_class(data=request.data)
        # valid = serializer.is_valid(raise_exception=True)
        # if valid:
        #     del serializer.validated_data['confirm_password']
        #     serializer.save(data=serializer.validated_data) 
        #     serializer.data['confirm_password']
        #     print("<<<<<<<<<<<<<<", user_otp, serializer.data)
        #     # if otp_send is is_verified:

        #     email = EmailMultiAlternatives('Confirmation mail.', f'verification otp is {user_otp}', 'arpansainiwins@gmail.com', [
        #         serializer.data['email']])
        #     email.send()
        #     status_code = status.HTTP_201_CREATED

        #     response = {
        #         'success': True,
        #         'statusCode': status_code,
        #         'message': 'User successfully registered!',
        #         'user': serializer.data
        #     }

        #     return Response(response, status=status_code)
        
val1 = None
class ChangePasswordView(APIView):
    def post(self, request):
        
        user_otp = random.randint(100000, 999999)
        global val1

        def val1():
            return user_otp

        serializer = resetpasswordSerializer(data=request.data)
        alldatas = {}
        if serializer.is_valid(raise_exception=True):
            mname = serializer.save()

            email = EmailMultiAlternatives('Confirmation mail.', f'verification otp is {user_otp}', 'arpansainiwins@gmail.com', [
                serializer.data['email']])
            email.send()
            
            pf = User.objects.filter()
            for item in pf:
                item.is_active = False
                item.save()

            alldatas['data'] = 'successfully registered'
            print(alldatas)
            return Response(alldatas)
        return Response('failed retry after some time')



class otpVerifyAPIView2(APIView):

    def post(self, request):
        ok1 = val1()

        serializer = otpVerifySerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            if serializer.data['otp'] == ok1:

                print("******  otp is matched  *******")

                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'otp is matched',
                    'user': serializer.data
                }
                return Response(response, tiv())
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
