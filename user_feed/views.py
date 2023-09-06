from rest_framework import generics
from constants.user_feed.views import QueryParam
from services.user_feed.views import get_feed_filter_data, get_sorted_feed
from user_feed.models import Note, Achievement, Advertisement
from user_feed.paginators import FeedPagination
from user_feed.serializers import FeedSerializer


class FeedView(generics.ListAPIView):
    """
        Вывод фида пользователя
    """
    serializer_class = FeedSerializer
    pagination_class = FeedPagination

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        search = self.request.query_params.get(QueryParam.Search)

        filter_data_for_notes, filter_data_for_achievements = get_feed_filter_data(user_id=user_id,
                                                                                   search=search)

        notes = Note.objects.filter(**filter_data_for_notes)
        
        achievements = Achievement.objects.filter(**filter_data_for_achievements)

        ads = Advertisement.objects.all()

        feed = get_sorted_feed(notes=notes,
                               achievements=achievements,
                               ads=ads)

        return feed

