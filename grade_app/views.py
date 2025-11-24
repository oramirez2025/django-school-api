from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_200_OK

from rest_framework.views import APIView
from .serializers import GradeSerializer
from .models import Grade

class All_grade(APIView):
    # Create a Grade with a Student, Subject, and a starting grade of 100.00
    def post(self, request):
        student = request.data['student']
        subject = request.data['subject']
        data = {
            "grade": 100.00,
            "a_subject": subject,
            "student": student
        }
        grade = GradeSerializer(data=data)
        if grade.is_valid():
            grade.save()
            return Response(grade.data, status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    # Update a Grades numeric value
    def put(self, request, id):
        try:
            grade = Grade.objects.get(id=id)
            ser_grade = GradeSerializer(grade, data=request.data, partial=True)
            if ser_grade.is_valid():
                ser_grade.save()
                return Response(status=HTTP_200_OK)
            else:
                return Response(ser_grade.errors, status=HTTP_400_BAD_REQUEST)
        except Grade.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

    # Delete a Grade for a Student and Subject
    def delete(self, request, id):
        try:
            grade = Grade.objects.get(id=id)
            grade.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Grade.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)