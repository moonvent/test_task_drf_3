from django.urls import path
from . import views


urlpatterns = [
     path('users/<int:pk>/', 
          views.FeedView.as_view(),
          name='feed'),
]
