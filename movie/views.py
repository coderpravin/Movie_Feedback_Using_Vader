from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ReviewMovieSerializer
from django.http import HttpResponse
from .models import ReviewMovie
from rest_framework.response import Response
from .utils import analyze_opinion
from rest_framework import status
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
    #print("data", serializer.data)  
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )


@api_view(["POST"])
def Add_movie(request):
    serializer = ReviewMovieSerializer(data = request.data)

    if serializer.is_valid():
        data = serializer.validated_data
        
        movie_name = data.get("movie_name")
        movie_review = data.get("movie_review")
        movie_rating = data.get("movie_rating")
        opinion = analyze_opinion(movie_review)
        
        ReviewMovie.objects.create(
            movie_name = movie_name, 
            movie_review = movie_review, 
            movie_rating = movie_rating, 
            movie_opinion = opinion
        )
        
        return Response(
            {"message":"saved success"},
            status= status.HTTP_201_CREATED
        )
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#UI for frontend
def review_page(request):
    if request.method == "POST":
        movie_name = request.POST.get("movie_name")
        movie_review = request.POST.get("movie_review")
        movie_rating = request.POST.get("movie_rating")
        
        opinion = analyze_opinion(movie_review)
        
        ReviewMovie.objects.create(
            movie_name = movie_name, 
            movie_review = movie_review,
            movie_rating = movie_rating,
            movie_opinion = opinion
        )
        
        return render(request, 'movie/index.html',{'opinion':opinion})
    return render(request, 'movie/index.html')
        
'''

queryset = ReviewMovie.objects.all()
    serializer = ReviewMovieSerializer(queryset, many=True)
    print("data", serializer.data)
'''

