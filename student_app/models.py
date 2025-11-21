from django.db import models
from django.core import validators as v
from .validators import validate_locker_combination, validate_name,validate_email
from django.core.exceptions import ValidationError
# from subject_app.models import Subject

class Student(models.Model):
    name = models.CharField(null=False, unique=False, validators=[validate_name])
    student_email = models.EmailField(null=False, unique=True, validators=[validate_email])
    personal_email = models.EmailField(null=True,unique=True)
    locker_number = models.IntegerField(null=False,unique=True,default=110,validators=[v.MinValueValidator(1),v.MaxValueValidator(200)])
    locker_combination = models.CharField(null=False,unique=False,default="12-12-12", validators=[validate_locker_combination])
    good_student = models.BooleanField(null=False,unique=False,default=True) 
    # subjects = models.ManyToManyField(Subject, related_name="students") # still need to validate (0 < x < 8)
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
    
    def student_status(self, new_student_value):
        self.good_student = new_student_value

    def add_subject(self, subject_id):
        if self.subjects.count() < 8:
            raise Exception("This students class schedule is full!")
        self.subjects.add(subject_id)
    def remove_subject(self, subject_id):
        if self.subjects.count() == 0:
            raise Exception("This students class schedule is empty!")
        self.subjects.remove(subject_id)