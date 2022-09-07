from django import forms

from web_app.models import Certificate


class CertificateForm(forms.ModelForm):
    school_name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    school_address = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    established_date = forms.CharField(
        widget=forms.TextInput({"class": "form-control"})
    )
    gender = forms.SelectMultiple(attrs={"class": "form-control form-control-lg"})
    student_name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    student_fathers_name = forms.CharField(
        widget=forms.TextInput({"class": "form-control"})
    )
    student_address = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    academic_year = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    program = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    passed_year = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    secured_gpa = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    date_of_birth = forms.DateField(widget=forms.DateInput({"class": "form-control"}))
    symbol_number = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    registration_number = forms.CharField(
        widget=forms.TextInput({"class": "form-control"})
    )
    issued_date = forms.CharField(widget=forms.TextInput({"class": "form-control"}))

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
            "issued_date",
        ]


class CertificateSearch(forms.Form):
    registration_number = forms.CharField(max_length=200)
