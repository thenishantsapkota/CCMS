import base64
import os
from django.shortcuts import render
from django.views import View
from ..models import Certificate
from os.path import exists


from ..forms import CertificateForm, CertificateSearch
from web_app.utils.util import create_certificate


class LandingView(View):
    def get(self, request):
        return render(request, "landing.html")


class CertificateView(View):
    form = CertificateForm

    def get(self, request):
        form = self.form()
        return render(request, "index.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            new_model = form.save()
            create_certificate(
                form.cleaned_data["school_name"],
                form.cleaned_data["school_address"],
                form.cleaned_data["established_date"],
                form.cleaned_data["gender"],
                form.cleaned_data["student_name"],
                form.cleaned_data["student_fathers_name"],
                form.cleaned_data["student_address"],
                form.cleaned_data["academic_year"],
                form.cleaned_data["program"],
                form.cleaned_data["passed_year"],
                form.cleaned_data["secured_gpa"],
                form.cleaned_data["date_of_birth"],
                form.cleaned_data["symbol_number"],
                form.cleaned_data["registration_number"],
                new_model.issued_date,
            )
            new_model.certificate = (
                f"media/certificate_{form.cleaned_data['registration_number']}.jpg"
            )
            new_model.save()

            with open(
                f"media/certificate_{form.cleaned_data['registration_number']}.jpg",
                "rb",
            ) as f:
                data = base64.b64encode(f.read()).decode("utf-8")

            ctx = {
                "image": data,
                "form": form,
                "title": "image",
                "filename": f"certificate_{form.cleaned_data['registration_number']}.jpg",
            }

            return render(request, "image.html", ctx)
        return render(request, "index.html", {"form": form})


class CertificateSearchView(View):
    form = CertificateSearch

    def get(self, request):
        form = self.form
        return render(request, "search.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        model = Certificate.objects.filter(
            registration_number=form.data.get("registration_number")
        )
        if not model.exists():
            try:
                os.system(
                    f"rm media/certificate_{form.data.get('registration_number')}.jpg"
                )
            except Exception:
                pass
        if model.exists() and not exists(
            f"media/certificate_{form.data.get('registration_number')}.jpg"
        ):
            data = model.first()
            create_certificate(
                data.school_name,
                data.school_address,
                data.established_date,
                data.gender,
                data.student_name,
                data.student_fathers_name,
                data.student_address,
                data.academic_year,
                data.program,
                data.passed_year,
                data.secured_gpa,
                data.date_of_birth,
                data.symbol_number,
                data.registration_number,
                data.issued_date,
            )

        try:
            with open(
                f"media/certificate_{form.data.get('registration_number')}.jpg", "rb"
            ) as f:
                data = base64.b64encode(f.read()).decode("utf-8")

            ctx = {
                "image": data,
                "form": form,
                "filename": f"certificate_{form.data.get('registration_number')}.jpg",
            }

            return render(request, "image.html", ctx)
        except Exception:
            form.add_error("registration_number", "Invalid registration number")
            pass
        return render(request, "search.html", {"form": form})
