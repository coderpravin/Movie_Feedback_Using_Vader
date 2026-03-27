from django.db import models

# Create your models here.

class ReviewMovie(models.Model):
    movie_name = models.CharField(max_length=250)
    movie_review = models.TextField()
    movie_opinion = models.CharField(max_length=250, blank=True)
    movie_rating = models.PositiveIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.movie_name}"     