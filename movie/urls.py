from django.urls import path
from .import views

urlpatterns = [
        path('submit', views.review_submit),
        path('home', views.review_list, name="review_list"),
        path('add', views.Add_movie, name="Add_movie"),
        
        path("", views.review_page, name="review-page")
]