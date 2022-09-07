from django.db import models
from versatileimagefield.fields import VersatileImageField


class GenderChoices(models.TextChoices):
    male = ("male", "Male")
    female = ("female", "Female")


# Create your models here.
class Certificate(models.Model):
    school_name = models.CharField(max_length=200)
    school_address = models.CharField(max_length=200)
    established_date = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GenderChoices.choices)
    student_name = models.CharField(max_length=200)
    student_fathers_name = models.CharField(max_length=200)
    student_address = models.CharField(max_length=200)
    academic_year = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    passed_year = models.CharField(max_length=200)
    secured_gpa = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    symbol_number = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200, unique=True)
    issued_date = models.CharField(max_length=200)

    certificate = VersatileImageField(upload_to="media/", null=True)
