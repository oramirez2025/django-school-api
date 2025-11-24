from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subject
from .serializers import SubjectSerializer


class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
