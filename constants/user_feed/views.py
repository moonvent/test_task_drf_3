from dataclasses import dataclass
from enum import Enum

from user_feed.models import Achievement, Advertisement, Note


class QueryParam(str, 
                 Enum):
    """
        Описание всех возможных параметров
    """
    Search = 'search'


@dataclass(frozen=True)
class Alias:
    FeedList = list[Note | Achievement | Advertisement]
