from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ReviewMovieSerializer
from django.http import HttpResponse
from .models import ReviewMovie
from rest_framework.response import Response
from .utils import analyze_opinion
# Create your views here.

@api_view(["POST"])
def review_submit(request):
    if request.method == "POST":
        serializer = ReviewMovieSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            movie_review = data.get("movie_review")
            opinion = analyze_opinion(movie_review)
            
            #print("Movie Rating", movie_rating)
            #print("Movie Opinion", opinion)
            print("opinion is", opinion)
            
            return Response({"message":"success", "opinion" :opinion})
            
            #print("The Review is", review_text)
        return Response(serializer.errors)
       

@api_view(["GET"])
def review_list(request):
    queryset = ReviewMovie.objects.all()
    serializer = ReviewMovieSerializer(queryset, many=True)
    print("data", serializer.data)  
    return HttpResponse("testing")



'''
queryset = ReviewMovie.objects.all()
    serializer = ReviewMovieSerializer(queryset, many=True)
    print("data", serializer.data)
'''

