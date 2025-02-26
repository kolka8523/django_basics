from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Director(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    picture = models.ImageField(upload_to='directors/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.FloatField(null=True, blank=True) 
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to='directors/', null=True, blank=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField(null=True, blank=True)
    created_ad = models.DateTimeField()


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_ad = models.DateTimeField()
