import base64
from django.shortcuts import render
from django.views import View


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
                form.cleaned_data["issued_date"],
            )
            new_model.certificate = (
                f"media/certificate_{form.cleaned_data['registration_number']}.png"
            )
            new_model.save()

            with open(
                f"media/certificate_{form.cleaned_data['registration_number']}.png",
                "rb",
            ) as f:
                data = base64.b64encode(f.read()).decode("utf-8")

            ctx = {"image": data, "form": form, "title": "image"}

            return render(request, "image.html", ctx)
        return render(request, "index.html", {"form": form})


class CertificateSearchView(View):
    form = CertificateSearch

    def get(self, request):
        form = self.form
        return render(request, "search.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        try:
            with open(
                f"media/certificate_{form.data.get('registration_number')}.png", "rb"
            ) as f:
                data = base64.b64encode(f.read()).decode("utf-8")

            ctx = {"image": data, "form": form}

            return render(request, "image.html", ctx)
        except Exception:
            form.add_error("registration_number", "Invalid registration number")
            pass
        return render(request, "search.html", {"form": form})
