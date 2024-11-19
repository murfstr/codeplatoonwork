from django.db import models
from django.core import validators as v

# Create your models here.
class Student (models.Model):
    name = models.CharField(blank=False)
    student_email = models.CharField(blank=False, validators=[v.EmailValidator()])
    personal_email = models.CharField(blank=True, validators=[v.EmailValidator()])
    locker_number = models.IntegerField(blank=False)
    locker_combination = models.CharField(blank=False)
    good_student = models.BooleanField(blank=False, null=False)