"""
    Описание общих констант для ошибок
"""


from enum import IntEnum


class ApiExceptionCode(IntEnum):
    """
        Описание внутренних ошибочных кодов прилоежния
    """
    # если пользователь передал айди не своего акка
    NotCorrectUserIdParam = 1

    # если пользователь пытается авторизироваться за несуществующим акком
    NotCorrectUserIdParamForAuth = 2

    # если появился новая модель для фида, но не была описана в сериализаторе
    NotCorrectFeedType = 3
