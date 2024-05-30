from django.contrib.auth import login, views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm, ProfileForm


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


def login_view(request):
    return auth_views.LoginView.as_view(
        template_name='authentication/login.html'
    )(request)


def logout_view(request):
    return auth_views.LogoutView.as_view()(request)


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile_edit")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, "authentication/profile_edit.html", {"form": form})
