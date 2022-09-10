from django.views import View
from django.shortcuts import render, redirect
from web_app.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
