from typing import Optional
from constants.user_feed.models import CACHE_FEED_QUERY_SET_KEY, CACHE_TIMEOUT
from constants.user_feed.views import Alias
from services.user_feed.views import get_feed_filter_data, get_sorted_feed
from user_feed.models import Achievement, Advertisement, Note, User
from django.core.cache import cache


def get_models_for_feed(user_id: int,
                        search: Optional[str] = None) -> Alias.FeedList:
    """
        Получение данных для фида пользователя
    """
    
    cache_key = CACHE_FEED_QUERY_SET_KEY.format(user_id, 
                                                search)

    # реализовал простенькое хеширование для запроса
    if cache_data := cache.get(cache_key):
        feed = cache_data

    else:
        filter_data_for_notes, filter_data_for_achievements = get_feed_filter_data(user_id=user_id,
                                                                                   search=search)

        # для хайлоада я бы дополнительно накинул бы условия для выборки по активной пагинационной странице

        notes = Note.objects.filter(**filter_data_for_notes)
        achievements = Achievement.objects.filter(**filter_data_for_achievements)
        ads = Advertisement.objects.all()

        feed = get_sorted_feed(notes=notes,
                               achievements=achievements,
                               ads=ads)

        cache.set(cache_key,
                  feed,
                  CACHE_TIMEOUT)

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

