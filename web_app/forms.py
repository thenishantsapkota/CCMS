from django import forms

from web_app.models import Certificate
from django.contrib.auth.forms import AuthenticationForm


class StylishForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-lg"})


class CertificateForm(StylishForm):

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
        ]


class CertificateSearch(forms.Form):
    registration_number = forms.CharField(
        max_length=200,
        widget=forms.TextInput({"class": "form-control form-control-lg"}),
    )


class LoginUserForm(forms.Form):
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
