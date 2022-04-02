from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Student_Management_App.models import Admin, Students, Teachers, CustomUser, Classes, Subjects
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# List All Students and create
class StudentList(APIView):

    def get(self, reuqest, format=None):
        student = Students.objects.select_related('class_id')
        serialized = StudentsSerializer(student, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):
        serialized = StudentsSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# List Teachers and create
class TeachersList(APIView):

    def get(self, reuqest, format=None):
        teachers = Teachers.objects.all()
        serialized = TeachersSerializer(teachers, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):
        serialized = TeachersSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# List All Classes and create
class ClassesList(APIView):

    def get(self, reuqest, format=None):
        classes = Classes.objects.all()
        serialized = ClassesSerializer(classes, many=True)
        return Response(serialized.data)

class SubjectsList(APIView):

    def get(self, reuqest, format=None):
        classes = Subjects.objects.all()
        serialized = SubjectsSerializer(classes, many=True)
        return Response(serialized.data)


# Teacher DetailView, Update, Delete 
class TeacherDetail(APIView):
    def get_object(self, pk):
        try:
            return Teachers.objects.get(pk=pk)
        except Teachers.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serialized = TeachersSerializer(teacher)
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serialized = TeachersSerializer(teacher, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serialized = TeachersSerializer(
            teacher, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Subject DetailView Update, Delete
class SubjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Subjects.objects.get(pk=pk)
        except Teachers.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        subject = self.get_object(pk)
        serialized = SubjectsSerializer(subject)
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        subject = self.get_object(pk)
        serialized = SubjectsSerializer(subject, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        subject = self.get_object(pk)
        serialized = SubjectsSerializer(
            subject, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
