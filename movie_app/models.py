from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    directors = models.ManyToManyField(Director, )
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)\


    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)