from datetime import datetime
from django.shortcuts import redirect, render

from django.contrib.auth import get_user_model, authenticate, login, logout
from web.forms import AuthorizationForm, RegistrationForm


User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request, "web/main.html", {
        "year": year
        })

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