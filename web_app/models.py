import os
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.db.models.signals import post_delete
from django.dispatch import receiver
from nepali_datetime import date

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
    issued_date = models.CharField(max_length=200,default=date.today().__str__(), null=True)    

    certificate = VersatileImageField(upload_to="media/", null=True)

    def __str__(self) -> str:
        return self.registration_number


@receiver(post_delete, sender=Certificate)
def signal_function_name(sender: Certificate, instance, using, **kwargs):
    ...
