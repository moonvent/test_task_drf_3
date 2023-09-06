from django.urls import path, re_path
from user_feed import views
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


urlpatterns = [
     path('users/<int:pk>/', 
          views.FeedView.as_view(),
          name='feed'),
     path('login/', 
          views.auth_view,
          name='login'),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="TestTask",
            default_version='v1',
            description="My API description",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
                schema_view.without_ui(cache_timeout=0),
                name='schema-json'),
        path('swagger/', 
             schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'),
        path('redoc/',
             schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc'),
    ]


