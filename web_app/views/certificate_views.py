import base64
import os
from django.shortcuts import render
from django.views import View
from ..models import Certificate
from os.path import exists
from django.db import transaction
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from ..forms import CertificateForm, CertificateSearch
from web_app.utils.util import create_certificate


class LandingView(View):
    def get(self, request):
        if not request.user.is_superuser:
            certificate_list = Certificate.objects.filter(user_id=request.user.id).order_by("student_name")
        else:
            certificate_list = Certificate.objects.all().order_by("student_name")
        paginator = Paginator(certificate_list, 5)
        page_number = request.GET.get("page")
        try:
            certificates = paginator.get_page(page_number)
        except PageNotAnInteger:
            certificates = paginator.page(1)
        except EmptyPage:
            certificates = paginator.page(paginator.num_pages)
        return render(request, "landing.html", {"certificates": certificates})


class CertificateView(View):
    form = CertificateForm

    def get(self, request):
        form = self.form()
        return render(request, "index.html", {"form": form})

    @transaction.atomic
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            new_model = form.save()
            new_model.user_id = request.user.id
            certificate_path = (
                f"certificate_{form.cleaned_data['registration_number']}.jpg"
            )
            create_certificate(
                request.user,
                form.cleaned_data["school_name"] or "",
                form.cleaned_data["school_address"] or request.user.institute.institute_address,
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
                form.cleaned_data["exam_board"],
            )
            new_model.certificate = certificate_path
            new_model.save()

            with open(
                f"media/{certificate_path}",
                "rb",
            ) as f:
                data = base64.b64encode(f.read()).decode("utf-8")

            ctx = {
                "image": data,
                "form": form,
                "title": "image",
                "filename": certificate_path,
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
        certificate_path = f"certificate_{form.data.get('registration_number')}.jpg"
        if not request.user.is_superuser:
            model = Certificate.objects.filter(
                registration_number=form.data.get("registration_number"),
                user_id=request.user.id,
            )
        else:
            model = Certificate.objects.filter(
                registration_number=form.data.get("registration_number")
            )
        if not model.exists():
            try:
                os.system(f"rm media/{certificate_path}")
            except Exception:
                pass
        if model.exists() and not exists(f"media/{certificate_path}"):
            data = model.first()
            create_certificate(
                request.user,
                data.school_name,
                data.school_address or request.user.institute.institute_address,
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
                data.exam_board,
            )

        if model.exists():
            try:
                with open(f"media/{certificate_path}", "rb") as f:
                    data = base64.b64encode(f.read()).decode("utf-8")

                ctx = {
                    "image": data,
                    "form": form,
                    "filename": certificate_path,
                }

                return render(request, "image.html", ctx)
            except Exception:
                form.add_error("registration_number", "Invalid registration number")
                pass

        form.add_error("registration_number", "Invalid registration number")
        return render(request, "search.html", {"form": form})
