from django.shortcuts import render
from .serializers import StudentAllSerializer, StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED

class All_students(APIView):
    def get(self, request):
        student = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(student.data)

class A_student(APIView):
    def get(self, request, id):
        student = StudentSerializer(Student.objects.get(id=id))
        return Response(student.data)
    

    # Create a Student with default values and no subject
    def post(self,request,id):
        ser_student = StudentSerializer(data=request.data)
        ser_student.save()
        if ser_student.is_valid():
            return Response(ser_student, status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    # Update a Students (all fields)
    def put(self, request, id):
        ser_student = StudentSerializer(data=request.data)
        if ser_student.is_valid():
            return Response(ser_student, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    # Delete a Student from the DB
    def delete(self,request,id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)


        

