from django.contrib import admin

from user_feed.models import Note, Advertisement, Achievement, User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = [field.name for field in Note._meta.fields]
    search_fields = ('title',
                     )


@admin.register(Advertisement)
class AdminAdvertisement(admin.ModelAdmin):
    list_display = [field.name for field in Advertisement._meta.fields]
    search_fields = ('title',
                     )


@admin.register(Achievement)
class AdminAchievement(admin.ModelAdmin):
    list_display = [field.name for field in Achievement._meta.fields]
    search_fields = ('title',
                     )

