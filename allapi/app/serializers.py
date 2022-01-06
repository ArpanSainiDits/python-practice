from django.contrib.auth import models
from rest_framework import serializers
from .models import User, otpVerify
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework import fields
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'mobile',

        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class otpVerifySerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = otpVerify
        fields = (
            'registerotp',
            'email'
        )


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid login credentialssssss")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,

            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


class forgetpasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    # otp = serializers.CharField(max_length=10, null=True, blank=True)

    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        # filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
        if User.objects.filter(email=email).exists():
            # if your username is existing get the query of your specific username
            user = User.objects.get(email=email)
            # then set the new password for your username
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {'error': 'please enter valid crendentials'})
