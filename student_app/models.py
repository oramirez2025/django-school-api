from django.db import models
from django.core import validators as v
from .validators import validate_locker_combination, validate_name,validate_email

class Student(models.Model):
    name = models.CharField(null=False, unique=False, validators=[validate_name])
    student_email = models.EmailField(null=False, unique=True, validators=[validate_email])
    personal_email = models.EmailField(null=True,unique=True) # no need 
    locker_number = models.IntegerField(null=False,unique=True,default=110,validators=[v.MinValueValidator(1),v.MaxValueValidator(200)])
    locker_combination = models.CharField(null=False,unique=False,default="12-12-12", validators=[validate_locker_combination])
    good_student = models.BooleanField(null=False,unique=False,default=True) # no need
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
    
    def student_status(self, new_student_value):
        self.good_student = new_student_value

