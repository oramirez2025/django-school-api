from django.db import models
from django.core import validators as v
from student_app.models import Student
from subject_app.models import Subject

class Grade(models.Model):
    grade = models.DecimalField(null=False,default=100.00, max_digits = 5, decimal_places=2,validators=[v.MinValueValidator(0.00),v.MaxValueValidator(100.00)])
    a_subject = models.ForeignKey(Subject, related_name="grades", on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name="grades",on_delete=models.CASCADE)
