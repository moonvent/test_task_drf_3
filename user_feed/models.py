from constants.user_feed.models import FieldLength, FoldersPath
from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    first_name = models.CharField(max_length=FieldLength.USER_FIRST_NAME)
    last_name = models.CharField(max_length=FieldLength.USER_LAST_NAME)
    django_user = models.OneToOneField(DjangoUser,
                                       on_delete=models.CASCADE)
    last_login = models.DateTimeField(null=True, 
                                      blank=True)


class Note(models.Model):
    class Meta:
        ordering = ('-created_at',)

    title = models.CharField(max_length=FieldLength.NOTE_TITLE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE)


class Achievement(models.Model):
    title = models.CharField(max_length=FieldLength.ACHIEVEMENT_TITLE)
    condition = models.TextField()
    icon = models.ImageField(upload_to=FoldersPath.ACHIEVEMENT_ICONS.value)
    user = models.ManyToManyField(User,
                                  related_name='achievements',
                                  help_text='Данным полем создаем связть многие ко многим')


class Advertisement(models.Model):
    class Meta:
        ordering = ('-published_at',)

    title = models.CharField(max_length=FieldLength.ADVERTISEMENT_TITLE)
    description = models.TextField()
    image = models.ImageField(upload_to=FoldersPath.ADVERTISEMENT_IMAGES.value)
    link = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True)


