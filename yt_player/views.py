import json

from yt_player.models import YTList, MusicRoom
from yt_player.serializer import YTListSerializer, MusicRoomSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class YTListView(viewsets.ModelViewSet):
    queryset = YTList.objects.all()
    serializer_class = YTListSerializer

    def get_queryset(self):
        return self.queryset.all()

    @action(detail=True, methods=['GET'])
    def get_list(self, request):
        lists = self.queryset.all()
        return Response(list(lists), status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def new_list(self, request):
        data = json.load(request.body)
        YTList.objects.create(
            list_id=data['data']['list_id'],
            edit_password=data['data']['edit_password'],
        )
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['DELETE'])
    def delete_list(self, request, pk=None):
        data = json.load(request.body)
        yt_list = YTList.objects.get(id=pk, edit_password=data['data']['edit_password'])
        yt_list.delete()
        return Response(list(data), status=status.HTTP_200_OK)


class MusicRoomView(viewsets.ModelViewSet):
    queryset = MusicRoom.objects.all()
    serializer_class = MusicRoomSerializer

    def get_queryset(self):
        return self.queryset.all()

    @action(detail=True, methods=['GET'])
    def get_room(self, request):
        rooms = self.queryset.all()
        return Response(list(rooms), status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def new_room(self, request, *args, **kwargs):
        data = json.load(request.body)
        rooms = list(self.queryset.all(room_id=data['data']['room_id']))
        if len(rooms) == 0:
            room = MusicRoom.objects.create(
                song_id=data['data']['song_id'],
                room_id=data['data']['room_id'],
            )
        else:
            room = rooms[0]
            room.is_play = False
            # room.now_time = 0
            room.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'])
    def update_room(self, request, pk=None):
        data = json.load(request.body)
        song_id = data['data']['song_id']
        now_time = data['data']['now_time']
        is_play = data['data']['is_play']

        room = self.queryset.first(id=pk)
        room.song_id = song_id
        room.now_time = now_time
        room.is_play = is_play
        room.save()
        return Response(status=status.HTTP_200_OK)
