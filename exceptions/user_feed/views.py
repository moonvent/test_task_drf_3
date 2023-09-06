from rest_framework.exceptions import APIException, status
from constants.exceptions.general import ApiExceptionCode
from constants.user_feed.views import ViewBodyDescription


class NotCorrectUserIdParam(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Не корректный айди переданный в запросе, вы пользователь с другим айди, и можете просматривать только свою ленту"
    default_code = ApiExceptionCode.NotCorrectUserIdParam


class NotCorrectUserIdParamForAuth(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ViewBodyDescription.UserIdNotFound
    default_code = ApiExceptionCode.NotCorrectUserIdParamForAuth

