from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    directors = models.ManyToManyField(Director, )
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


stars = ((i, i * '8') for i in range(1, 6))


class Review(models.Model):
    text = models.TextField(choices=stars)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    star = models.IntegerField(default=0)

    def __str__(self):
        return self.text
