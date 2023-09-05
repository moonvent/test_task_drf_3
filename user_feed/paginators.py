"""
    Пагинаторы используемые в приложении
"""


from rest_framework import pagination

from constants.user_feed.paginators import PaginationSize


class FeedPagination(pagination.PageNumberPagination):
    page_size = PaginationSize.Feed
    page_size_query_param = 'page_size'

