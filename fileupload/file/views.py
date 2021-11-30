from django.shortcuts import render
from rest_framework import serializers
from .models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import profileserializer

# Create your views here.


class profileView(APIView):
    def post(self, request):
        serializer = profileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Done'})
        return Response(serializer.error)
    
    def get(self, request):
        data = Profile.objects.all()
        serializer = profileserializer(data, many = True)
        return Response(serializer.data)    