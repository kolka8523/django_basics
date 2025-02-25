from django.contrib import admin
from django.urls import path
from web.views import *


urlpatterns = [
    path('', main_view, name='main'),
    path("registration", registration_view, name='registration'),
    path("authorization", authorization_view, name='authorization'),
]