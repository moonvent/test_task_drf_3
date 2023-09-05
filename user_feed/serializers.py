from rest_framework import serializers
from user_feed.models import Achievement, Advertisement, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class UniversalSerializer(serializers.Serializer):

    model_type = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    def get_model_type(self, obj):
        return obj.__class__.__name__

    def get_details(self, obj):
        if isinstance(obj, Note):
            return NoteSerializer(obj).data

        if isinstance(obj, Advertisement):
            return AdvertisementSerializer(obj).data

        if isinstance(obj, Achievement):
            return AchievementSerializer(obj).data
