"""
    Описание констант для вьюх
"""


from dataclasses import dataclass
from enum import Enum

from rest_framework.exceptions import status

from user_feed.models import Achievement, Advertisement, Note

from drf_yasg import openapi


class QueryParam(str, 
                 Enum):
    """
        Описание всех возможных параметров
    """
    Search = 'search'


@dataclass(frozen=True)
class Alias:
    """
        Алиасы типов, для более коротного и читаемого размещения типов
    """
    FeedList = list[Note | Achievement | Advertisement]


class ViewBodyDescription(str, 
                          Enum):
    """
        Описание тел возвращаемых запросов
    """
    Logged = 'Аутентифицирован'
    UserIdNotFound = 'Айди пользователя не найден'


@dataclass(frozen=True)
class OpenApiSchema:
    """
        Описание схем для свагера
    """
    Auth = dict(operation_description="Авторизация для проверки на доступность чтения только ленты пользователя",
        method='get',
        manual_parameters=[
            openapi.Parameter('user_id',
                              openapi.IN_QUERY,
                              description="Айди пользователя", 
                              type=openapi.TYPE_INTEGER),
        ],
        responses={status.HTTP_200_OK: ViewBodyDescription.Logged, 
                   status.HTTP_400_BAD_REQUEST: ViewBodyDescription.UserIdNotFound}
    )
