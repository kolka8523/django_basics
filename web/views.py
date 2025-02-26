from datetime import datetime
from django.shortcuts import redirect, render

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from web.forms import *


User = get_user_model()

def is_staff_user(user):
    return user.is_staff

def main_view(request):
    movies = Movie.objects.all()
    return render(request, "web/main.html", {'movies': movies})

def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form,
        "is_success": is_success
        })
    
def authorization_view(request):
    form = AuthorizationForm()
    if request.method == 'POST':
        form = AuthorizationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Пользователь не найден")
            else:
                login(request, user)
                return redirect('main')
    return render(request, "web/authorization.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("main")

def review_add_view(request):
    form = ReviewForm()
    return render(request, "web/review_form.html", {"form": form})

def add_instance(request, form):
    is_success = False
    if request.method == 'POST':
        if form.is_valid():
            print(form)
            form.save()
            is_success = True
        else:
            is_success = False
    return render(request, "web/add_entity.html", {
        "form": form,
        "is_success": is_success
        })

@user_passes_test(is_staff_user)
def genre_add_view(request):
    return add_instance(request, GenreForm(request.POST))

@user_passes_test(is_staff_user)
def director_add_view(request):
    return add_instance(request, DirectorForm(request.POST))

@user_passes_test(is_staff_user)
def movie_add_view(request):
    return add_instance(request, MovieForm(request.POST))
