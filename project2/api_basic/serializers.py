from rest_framework import fields, serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    course = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance
    
        
class StudentSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'email', 'course']
        fields = '__all__'
        

        
        
        
        
        
        