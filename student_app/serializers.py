from .models import Student

from rest_framework import serializers
from subject_app.serializers import SubjectSerializer
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Student
        fields = [
            "name",
            "student_email",
            "personal_email",
            "locker_number",
            "locker_combination",
            "good_student",
            "subjects",
        ]
    
    # Create a Student with default values and no subject
    def post(self,request,id):
        pass

    # Update a Students (all fields)
    def put(self,request,id):
        pass

    # Delete a Student from the DB
    def delete(self,request,id):
        student = Student.objects.get(id=id)
        

class StudentAllSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Student
        fields = [
            "name",
            "student_email",
            "personal_email",
            "locker_number",
            "locker_combination",
            "good_student",
            "subjects",
        ]