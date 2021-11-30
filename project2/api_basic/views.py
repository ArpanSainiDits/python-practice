from codecs import lookup
from django.db.models import query
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework import authentication
from rest_framework import permissions
from .serializers import StudentSerializer, StudentSerializerModel
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from.models import Student
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_list_or_404






# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializerModel
    queryset = Student.objects.all()


class StudentGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = StudentSerializerModel
    queryset = Student.objects.all()




class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        students = Student.objects.all()
        serializer = StudentSerializerModel(students, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializerModel(student)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    
    serializer_class = StudentSerializerModel
    queryset = Student.objects.all()
    
    lookup_field = 'id'
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]

    # permission_classes = [IsAuthenticated]
     
    
    def get(self, request, id= None):
        if id: 
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id= None):
        return self.update(request, id)
    
    def delete(self, request, id = None):
        return self.destroy(request, id)
    
    


@csrf_exempt
def student_list(request):
    
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializerModel(students, many=True)
        return JsonResponse(serializer.data, safe= False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializerModel(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    

@api_view(['GET', 'POST'])
def student_list1(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializerModel(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
       
        serializer = StudentSerializerModel(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist :
        return HttpResponse(status = 400)
    
    if request.method == 'GET':
        serializer = StudentSerializerModel(student)   
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializerModel(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail1(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializerModel(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = StudentSerializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StudentAPIView(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializerModel(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializerModel(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        student = self.get_object(id) 
        serializer = StudentSerializerModel(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   
    
            