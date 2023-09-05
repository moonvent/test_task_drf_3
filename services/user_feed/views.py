from typing import Optional


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


