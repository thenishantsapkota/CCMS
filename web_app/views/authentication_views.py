from django.views import View
from django.shortcuts import render, redirect
from web_app.forms import LoginUserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from web_app.models import User


class LoginView(View):
    form = LoginUserForm

    def get(self, request):
        form = self.form()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        username = form.data.get("username")
        password = form.data.get("password")
        remember_me = form.data.get("remember_me")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            messages.success(request, "Logged in successfully!")
            return redirect("/")
        form.add_error("password", "Invalid username or password")

        return render(request, "login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect("/login")


class ProfileView(View):
    def get(self, request):
        return render(request, "profile.html")


class EditProfileView(View):
    form = ProfileForm

    def get(self, request):
        form = self.form()
        return render(request, "edit_profile.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.first_name = form.data.get("first_name")
            user.last_name = form.data.get("last_name")
            if institute_name := form.data.get("institute_name"):
                user.institute.institute_name = institute_name
            if institute_address := form.data.get("institute_address"):
                user.institute.institute_address = institute_address
            if logo := request.FILES.get("institute_logo"):
                user.institute.institute_logo = logo
            if avatar := request.FILES.get("avatar"):
                user.avatar = avatar
            user.save()
            user.institute.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect(to="profile")

        return render(request, "edit_profile.html", {"form": form})
