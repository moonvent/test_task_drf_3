from rest_framework import serializers
from constants.user_feed.serializers import EventMessages
from constants.user_feed.views import Alias
from exceptions.user_feed.serializers import NotCorrectFeedType
from user_feed.models import Achievement, Advertisement, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title',
                  'body',
                  'created_at'
                  )


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('title',
                  'condition',
                  'icon'
                  )


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title',
                  'description',
                  'image',
                  'link',
                  'published_at'
                  )


class FeedSerializer(serializers.Serializer):

    model_type = serializers.SerializerMethodField()
    event_message = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    # кешируем сериалайзеры чтоб быстро к ним обращаться
    __cached_serializers = {
        Note: NoteSerializer,
        Advertisement: AdvertisementSerializer,
        Achievement: AchievementSerializer,

    }

    def get_model_type(self, 
                       obj: Alias.FeedEvent):
        """
            Выводим название модели
        """
        return obj.__class__.__name__

    def get_event_message(self,
                          obj: Alias.FeedEvent):
        """
            Выводим текст события которое привязано к модели
        """
        obj_type = type(obj)

        if message := EventMessages.get(obj_type):
            return message

        raise NotCorrectFeedType

    def get_details(self,
                    obj: Alias.FeedEvent):
        """
            Обрабатываем данные самой модели
        """
        obj_type = type(obj)

        if serializer := self.__cached_serializers.get(obj_type):
            return serializer(obj).data

        raise NotCorrectFeedType

