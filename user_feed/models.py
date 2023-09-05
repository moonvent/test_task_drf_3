from constants.user_feed.models import FieldLength, FoldersPath
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=FieldLength.USER_FIRST_NAME)
    last_name = models.CharField(max_length=FieldLength.USER_LAST_NAME)


class Note(models.Model):
    title = models.CharField(max_length=FieldLength.NOTE_TITLE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE)


class Achievement(models.Model):
    title = models.CharField(max_length=FieldLength.ACHIEVEMENT_TITLE)
    condition = models.TextField()
    icon = models.ImageField(upload_to=FoldersPath.ACHIEVEMENT_ICONS)
    user = models.ManyToManyField(User,
                                  related_name='achievements')


class Advertisement(models.Model):
    title = models.CharField(max_length=FieldLength.ADVERTISEMENT_TITLE)
    description = models.TextField()
    image = models.ImageField(upload_to=FoldersPath.ADVERTISEMENT_IMAGES)
    link = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True)


