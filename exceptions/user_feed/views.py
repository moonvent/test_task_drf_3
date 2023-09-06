from rest_framework.exceptions import APIException, status
from constants.user_feed.views import ViewBodyDescription


class NotCorrectUserIdParam(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Не корректный айди переданный в запросе, вы пользователь с другим айди, и можете просматривать только свою ленту"
    default_code = 1


class NotCorrectUserIdParamForAuth(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ViewBodyDescription.UserIdNotFound
    default_code = 2

