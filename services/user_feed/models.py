from typing import Optional
from django.contrib.auth.models import ContentType

from django.db.models import Q
from constants.user_feed.views import Alias
from services.user_feed.views import get_feed_filter_data
from user_feed.models import Advertisement, User, FeedElement


def get_models_for_feed(user: User,
                        search: Optional[str] = None) -> Alias.FeedList:
    """
        Получение данных для фида пользователя
    """
    
    filter_data_for_notes, filter_data_for_achievements = get_feed_filter_data(user=user,
                                                                               search=search)

    advertisment_ctype = ContentType.objects.get_for_model(Advertisement)
    filter_condition = (Q(**filter_data_for_notes) | 
        Q(**filter_data_for_achievements) | 
        Q(polymorphic_ctype=advertisment_ctype))

    feed = (FeedElement
        .objects
        .filter(filter_condition)
    )

    return feed


def get_django_user(user_id: int) -> Optional[User]:
    """
        Получение сущности пользователя из Джанго ауф системы
    """
    users = (User
        .objects
        .filter(id=user_id)
    )

    if users:
        user = users.first()
        return user

