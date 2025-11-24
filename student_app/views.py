from django.shortcuts import render
from .serializers import StudentAllSerializer, StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response

class All_students(APIView):
    def get(self, request):
        student = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(student.data)

class A_student(APIView):
    def get(self, request, id):
        student = StudentSerializer(Student.objects.get(id=id))
        return Response(student.data)
        

