from dataclasses import fields
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from Student_Management_App.models import *
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class AdminSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = fields = '__all__'


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class ClassesSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer(many=True, read_only=True)
    class Meta:
        model = Classes
        fields = '__all__'


class TeachersSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer(many=True, read_only=True)
    class Meta:
        model = Teachers
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class_ = ClassesSerializer(many=True, read_only=True)
    class Meta:
        model = Students
        fields = '__all__'
         
     
     
     
     
    
    