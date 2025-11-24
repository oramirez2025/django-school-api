from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Subject
from .serializers import SubjectSerializer

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK


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

    # Create a Subject with default values
    def post(self, request):
        ser_sub = SubjectSerializer()
        if ser_sub.is_valid():
            return Response(ser_sub, status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    
    # Update the name or professor of a Subject
    def put(self, request, professor, subject):
        data = {}
        if not subject:
            data['subject_name'] = subject
        if not professor:
            data['professor'] = professor
        
        ser_subject = SubjectSerializer(data=data)
        if ser_subject.is_valid():
            return Response(ser_subject, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

