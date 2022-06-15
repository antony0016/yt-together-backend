from rest_framework import serializers
from yt_player.models import YTList, MusicRoom


class YTListSerializer(serializers.ModelSerializer):
    class Meta:
        model = YTList
        fields = '__all__'


class MusicRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicRoom
        fields = '__all__'
