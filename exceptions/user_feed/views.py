from rest_framework.exceptions import APIException, status


class NotCorrectUserIdParam(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Не корректный айди переданный в запросе, вы пользователь с другим айди, и можете просматривать только свою ленту"
    default_code = '1'

