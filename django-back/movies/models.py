from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name =  models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    adult = models.BooleanField(null=True)
    overview = models.TextField(null=True)
    original_language = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    def __str__(self):
        return self.title

class Review(models.Model):
    score = models.IntegerField()
    content = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews", on_delete=models.CASCADE)
    # user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_reviews')