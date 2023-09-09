from django.contrib.auth import login, logout
from django.core.handlers.asgi import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from loguru import logger
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotAuthenticated
from constants.user_feed.views import Alias, OpenApiSchema, QueryParam, ViewBodyDescription
from exceptions.user_feed.views import NotCorrectUserIdParam
from services.user_feed.models import get_django_user, get_models_for_feed
from user_feed.paginators import FeedPagination
from user_feed.serializers import FeedSerializer
from drf_yasg.utils import swagger_auto_schema


class FeedView(generics.ListAPIView):
    """
        Вывод фида пользователя
    """
    serializer_class = FeedSerializer
    pagination_class = FeedPagination

    def get_queryset(self) -> Alias.FeedList:

        auth_user = self.request.user
        if not auth_user.is_authenticated:
            raise NotAuthenticated

        user_id = self.kwargs['pk']

        if user_id != auth_user.id:
            raise NotCorrectUserIdParam

        search = self.request.query_params.get(QueryParam.Search)

        feed = get_models_for_feed(search=search,
                                   user=auth_user)  

        return feed


@swagger_auto_schema(**OpenApiSchema.Auth)
@api_view(['GET'])
def auth_view(request: WSGIRequest) -> HttpResponse:
    """
        Ручка для быстрой авторизации
    """
    user_id = request.GET.get('user_id')
    
    if django_user := get_django_user(user_id=user_id):

        if request.user.is_authenticated:
            logout(request)
        
        login(request, 
              django_user)

        return HttpResponse(ViewBodyDescription.Logged)

    raise NotCorrectUserIdParam



