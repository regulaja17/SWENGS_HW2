from django.contrib import admin

# Register your models here.
from music.models import Label, Song, Musician


class LabelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'origin_country']
admin.site.register(Label, LabelAdmin)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'duration', 'label')

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('alias', 'first_name', 'last_name')