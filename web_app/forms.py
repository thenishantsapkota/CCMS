from django import forms

from web_app.models import Certificate
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class StylishForm(forms.Form):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-lg"})


class StylishModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-lg"})


class CertificateForm(StylishModelForm):

    school_name = forms.CharField(max_length=200)
    school_address = forms.CharField(max_length=200)
    established_date = forms.CharField(max_length=200)
    gender = forms.Select()
    student_name = forms.CharField(max_length=200)
    student_fathers_name = forms.CharField(max_length=200)
    student_address = forms.CharField(max_length=200)
    academic_year = forms.CharField(max_length=200)
    program = forms.CharField(max_length=200)
    passed_year = forms.CharField(max_length=200)
    secured_gpa = forms.CharField(max_length=200)
    date_of_birth = forms.DateField(
        widget=forms.DateInput({"id": "nepali-datepicker"}, format=("%d-%m-%Y"))
    )
    symbol_number = forms.CharField(max_length=200)
    registration_number = forms.CharField(max_length=200)
    exam_board = forms.CharField(max_length=50)

    class Meta:
        model = Certificate
        fields = [
            "school_name",
            "school_address",
            "established_date",
            "gender",
            "student_name",
            "student_fathers_name",
            "student_address",
            "academic_year",
            "program",
            "passed_year",
            "secured_gpa",
            "date_of_birth",
            "symbol_number",
            "registration_number",
            "exam_board",
        ]


class CertificateSearch(StylishForm):
    registration_number = forms.CharField(
        max_length=200,
        widget=forms.TextInput({"class": "form-control form-control-lg"}),
    )


class LoginUserForm(StylishForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Enter your username",
            }
        ),
    )

    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Enter your password",
            }
        ),
    )

    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput({"class": "form-check-input"})
    )


class ProfileForm(StylishForm):
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=50)
    institute_logo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            {
                "accept": "image/png",
                "name": "logoInstitute",
                "onchange": "validateImageType()",
            }
        ),
    )
    institute_name = forms.CharField(
        max_length=200,
    )


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("username", "password", "is_active", "is_superuser")

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
