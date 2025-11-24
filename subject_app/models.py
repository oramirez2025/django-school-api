from django.db import models
from .validators import validate_professor_name, validate_subject_name
from django.core import validators as v

class Subject(models.Model):
    subject_name = models.CharField(null=False, unique=True, validators=[validate_subject_name]) 
    professor = models.CharField(null=False, validators = [validate_professor_name])


    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()}"
    

    # we need to drop the entry in the student model 
    def add_a_student(self,student_id):
        if self.students.count() >= 31:
            raise Exception("This subject is full!")
        self.students.add(student_id)

    def drop_a_student(self,student_id):
        if self.students.count() == 0:
            raise Exception("This subject is empty!")
        self.students.remove(student_id)
    