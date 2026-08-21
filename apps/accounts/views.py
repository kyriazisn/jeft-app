from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")
    return render(request, "accounts/signup.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(request, email=form.cleaned_data["email"], password=form.cleaned_data["password"])
        if user is not None:
            login(request, user)
            return redirect("home")
        form.add_error(None, "Invalid email or password.")
    return render(request, "accounts/login.html", {"form": form})


def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return render(request, "accounts/logout.html")
