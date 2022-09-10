from django import forms

from web_app.models import Certificate


class CertificateForm(forms.ModelForm):
    school_name = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    school_address = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    established_date = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    gender = forms.Select(attrs={"class": "form-select form-select-lg"})
    student_name = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    student_fathers_name = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    student_address = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    academic_year = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    program = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    passed_year = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    secured_gpa = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            {"class": "form-control form-control-lg", "id": "nepali-datepicker"}, format=("%d-%m-%Y")
        )
    )
    symbol_number = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )
    registration_number = forms.CharField(
        widget=forms.TextInput({"class": "form-control form-control-lg"})
    )

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
