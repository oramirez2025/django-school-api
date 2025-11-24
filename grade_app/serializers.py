from rest_framework import serializers
from .models import Grade
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        field = '__all__'
