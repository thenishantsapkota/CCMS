import os
from django.db import models
from versatileimagefield.fields import VersatileImageField
from nepali_datetime import date
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from .managers import UserManager


class GenderChoices(models.TextChoices):
    male = ("male", "Male")
    female = ("female", "Female")


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    avatar = models.ImageField(upload_to="profile/", blank=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    institute_name = models.CharField(max_length=100, blank=True)
    institute_logo = models.ImageField(upload_to="logos/", blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name


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
    issued_date = models.CharField(
        max_length=200, default=date.today().__str__(), null=True
    )
    exam_board = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    certificate = VersatileImageField(upload_to="media/", null=True)

    def __str__(self) -> str:
        return self.registration_number
