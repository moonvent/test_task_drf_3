from enum import Enum


class QueryParam(str, 
                 Enum):
    """
        Описание всех возможных параметров
    """
    Search = 'search'
