from enum import Enum

from user_feed.models import Achievement, Advertisement, Note


class _FeedEventMessage(str, 
                       Enum):
    """
        Описание всех сообщений об ивентах
    """
    Note = 'Пользователь написал заметку'
    Advertisement = 'Рекламное объявление'
    Achievement = 'Пользователь получил достижение'


# словарь, для быстрого получения 
EventMessages = {
    Achievement: _FeedEventMessage.Achievement,
    Note: _FeedEventMessage.Note,
    Advertisement: _FeedEventMessage.Advertisement,
}
