from django.contrib import admin
from django.urls import path
from web.views import *


urlpatterns = [
    path('',                main_view,          name='main'),
    path("registration/",   registration_view,  name='registration'),
    path("authorization/",  authorization_view, name='authorization'),
    path("logout/",         logout_view,        name='logout'),
    path("reviews/add/",    review_add_view,    name='reviews_add'),
    path("staff/genre/",    genre_add_view,     name='genre_add'),
    path("staff/director/", director_add_view,  name='director_add'),
    path("staff/movie/",    movie_add_view,     name='movie_add'),
]
