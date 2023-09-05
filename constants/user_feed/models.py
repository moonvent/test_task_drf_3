from enum import Enum, IntEnum


class FieldLength(IntEnum):
    """
        Описание длин полей в базе данных
    """

    USER_FIRST_NAME = 32
    USER_LAST_NAME = 32

    NOTE_TITLE = 32

    ACHIEVEMENT_TITLE = 32
    
    ADVERTISEMENT_TITLE = 32


class FoldersPath(str, 
                  Enum):
    """
        Описание путей к папкам для сохранения какого-либо контента
    """
    ACHIEVEMENT_ICONS = 'icons/'
    ADVERTISEMENT_IMAGES = 'ads/'

