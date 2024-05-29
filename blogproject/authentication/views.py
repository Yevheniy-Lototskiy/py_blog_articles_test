from django.shortcuts import render, redirect
from django.contrib.auth import login, views as auth_views
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "authentication/register.html", {"form": form})
