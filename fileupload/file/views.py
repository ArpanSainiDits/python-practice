from django.shortcuts import render
from rest_framework import serializers
from .models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializer import profileserializer
from rest_framework import status
from django.core.exceptions import ValidationError
# Create your views here.


class profileView(APIView):
    def post(self, request):
        serializer = profileserializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Done'})
        else:
            return Response(serializer.errors)
    
    def get(self, request):
        data = Profile.objects.all()
        serializer = profileserializer(data, many = True)
        return Response(serializer.data)    
    

class profileView1(APIView):
    def get_object(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        profile = self.get_object(id)
        serializer = profileserializer(profile)
        return Response(serializer.data)

    def put(self, request, id):
        profile = self.get_object(id)
        serializer = profileserializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, id):
        profile = self.get_object(id)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

