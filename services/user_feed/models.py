from typing import Optional
from constants.user_feed.views import Alias
from services.user_feed.views import get_feed_filter_data, get_sorted_feed
from user_feed.models import Achievement, Advertisement, Note, User, DjangoUser


def get_models_for_feed(user_id: int,
                        search: Optional[str] = None) -> Alias.FeedList:
    """
        Получение данных для фида пользователя
    """
    filter_data_for_notes, filter_data_for_achievements = get_feed_filter_data(user_id=user_id,
                                                                               search=search)

    # для хайлоада я бы дополнительно накинул бы условия для выборки по активной пагинационной странице

    notes = Note.objects.filter(**filter_data_for_notes)
    achievements = Achievement.objects.filter(**filter_data_for_achievements)
    ads = Advertisement.objects.all()

    feed = get_sorted_feed(notes=notes,
                           achievements=achievements,
                           ads=ads)
    return feed


def get_django_user(user_id: int) -> Optional[DjangoUser]:
    """
        Получение сущности пользователя из Джанго ауф системы
    """
    users = (User
        .objects
        .filter(id=user_id)
    )

    if users:
        django_user = users.first()
        return django_user

