from django.contrib.auth import login
from django.core.handlers.asgi import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import generics
from rest_framework.exceptions import NotAuthenticated
from constants.user_feed.views import Alias, QueryParam
from services.user_feed.models import get_django_user, get_models_for_feed
from user_feed.paginators import FeedPagination
from user_feed.serializers import FeedSerializer


class FeedView(generics.ListAPIView):
    """
        Вывод фида пользователя
    """
    serializer_class = FeedSerializer
    pagination_class = FeedPagination

    def get_queryset(self) -> Alias.FeedList:
        if not self.request.user.is_authenticated:
            raise NotAuthenticated

        user_id = self.request.user.id
        search = self.request.query_params.get(QueryParam.Search)

        feed = get_models_for_feed(user_id=user_id,
                                   search=search)  

        return feed


def auth_view(request: WSGIRequest) -> HttpResponse:
    """
        Ручка для быстрой авторизации
    """
    user_id = request.GET.get('user_id')
    django_user = get_django_user(user_id=user_id)

    login(request, 
          django_user)

    return HttpResponse('Logged in')



