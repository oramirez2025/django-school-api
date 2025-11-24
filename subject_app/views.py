from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Subject
from .serializers import SubjectSerializer


class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class A_subject(APIView):
    def get(self, request, subject):
        try:
            subject = Subject.objects.get(subject_name=subject)
        except Subject.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
