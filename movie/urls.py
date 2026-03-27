from django.urls import path
from .import views

urlpatterns = [
        path('submit', views.review_submit),
        path('home', views.review_list, name="review_list"),
]