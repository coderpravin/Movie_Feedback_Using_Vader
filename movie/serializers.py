from rest_framework import serializers
from .models import ReviewMovie

class ReviewMovieSerializer(serializers.Serializer):
    movie_name = serializers.CharField(max_length=250)
    movie_review = serializers.CharField()
    movie_opinion = serializers.CharField(read_only=True)
    movie_rating = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(read_only=True)


