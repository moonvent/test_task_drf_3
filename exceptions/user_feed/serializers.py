from rest_framework.exceptions import APIException, status

from constants.exceptions.general import ApiExceptionCode


class NotCorrectFeedType(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Ошибка, нельзя выводить в фид какие-то дополнительные сущности кроме `Note`, `Advertismend` и `Achievement`"
    default_code = ApiExceptionCode.NotCorrectFeedType

