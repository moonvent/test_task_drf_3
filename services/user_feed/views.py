from itertools import zip_longest
from typing import Optional
from constants.user_feed.views import Alias

from user_feed.models import Achievement, Advertisement, FeedElement, Note, User


def get_feed_filter_data(user: User, 
                         search: Optional[str]) -> tuple[dict, dict]:
    """
        Получение словаря с данными для фильтра в запросах

        Returns:
            tuple[dict, dict]: кортеж с двумя словарями,
                один для фильтра Notes модели,
                другой для фильтра Achievments модели
    """

    if search:
        # единственное что, какой* поиск нужен, ибо я подумал о wildcard а он же очень 
        # до производительности жористый, но, тут нужно просто деталей поболее

        filter_data_for_notes = dict(note__title__icontains=search,
                                     not__user=user)

        filter_data_for_achievements = dict(achievement__title__icontains=search,
                                            achievement__user__id=user)
    else:
        filter_data_for_notes = dict(note__user=user)
        filter_data_for_achievements = dict(achievement__user=user)

    return filter_data_for_notes, filter_data_for_achievements


def get_sorted_feed(feed_elements: list[FeedElement]) -> Alias.FeedList:
    """
        Распределение контента, а именно 1 новость, 1 ачивка, 1 реклама, 
            чтоб не было одноготипного контента

        Returns:
            list[Note | Achievement | Advertisement]: список с сущностями в отсортированном порядке
    """
    sorted_feed_list = []
    
    for note, achievement, ad in zip_longest(notes, 
                                             achievements, 
                                             ads):
        models = (note, achievement, ad)

        if sum([bool(model) for model in models]) < 2:
            break

        sorted_feed_list.extend([model for model in models if model])

    return sorted_feed_list
    
