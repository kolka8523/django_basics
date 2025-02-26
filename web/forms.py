from django import forms
from django.contrib.auth import get_user_model

from web.models import *

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', "Passwords are not the same")
        return cleaned_data
    

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")
        widgets = {
            'password': forms.PasswordInput()
        }
        
        
class AuthorizationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ('name', 'birthday', 'picture')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'director', 'genre', 'release_date', 'description', 'poster')
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }


class ReviewForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)
    class Meta:
        model = Review
        fields = ("movie", "rating", "text")
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'text': forms.Textarea(attrs={'rows': 4})
        }
