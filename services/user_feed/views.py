from itertools import zip_longest
from typing import Optional
from constants.user_feed.views import Alias

from user_feed.models import Achievement, Advertisement, Note


def get_feed_filter_data(user_id: int, 
                         search: Optional[str]) -> tuple[dict, dict]:
    """
        Получение словаря с данными для фильтра в запросах

        Returns:
            tuple[dict, dict]: кортеж с двумя словарями,
                один для фильтра Notes модели,
                другой для фильтра Achievments модели
    """

    if search:
        filter_data_for_notes = dict(title__icontains=search,
                                     user_id=user_id)

        filter_data_for_achievements = dict(name__icontains=search,
                                            user_id=user_id)
    else:
        filter_data_for_notes = dict(user_id=user_id)
        filter_data_for_achievements = dict(user__id=user_id)

    return filter_data_for_notes, filter_data_for_achievements


def get_sorted_feed(notes: list[Note],
                    achievements: list[Achievement],
                    ads: list[Advertisement]) -> Alias.FeedList:
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
    
