from django.db import models

class Student(models.Model):
    name = models.CharField(null=False)
    student_email = models.EmailField(null=False)
    personal_email = models.EmailField(null=True)
    locker_number = models.IntegerField(null=False)
    locker_combination = models.CharField(null=False)
    good_student = models.BooleanField(null=False)

