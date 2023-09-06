from django.urls import path
from user_feed import views


urlpatterns = [
     path('users/<int:pk>/', 
          views.FeedView.as_view(),
          name='feed'),
     path('login/', 
          views.auth_view,
          name='login'),
]
