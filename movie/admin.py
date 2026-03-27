from django.contrib import admin
from .models import ReviewMovie

# Register your models here.
class ReviewMovieAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "movie_review", "movie_opinion")
    
admin.site.register(ReviewMovie, ReviewMovieAdmin)