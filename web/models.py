from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Director(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField
    description = models.TextField
    poster_url = models.CharField(max_length=150)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField
    text = models.TextField
    created_ad = models.DateTimeField


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField
    created_ad = models.DateTimeField
