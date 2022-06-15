from django.db import models


# Create your models here.
class YTList(models.Model):
    list_id = models.TextField(unique=True)
    list_name = models.TextField(blank=True)
    edit_password = models.TextField()

    class Meta:
        db_table = "yt_list"


class MusicRoom(models.Model):
    song_id = models.TextField()
    room_id = models.TextField(unique=True)
    now_time = models.FloatField(default=0)
    is_play = models.BooleanField(default=False)

    class Meta:
        db_table = 'music_room'
