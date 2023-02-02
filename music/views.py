from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models  import Music
from music.serializers import MusicSerializer


@api_view(['GET'])
def get_hello(request):
    return Response('Hello world')


@api_view(['GET'])
def get_music(request):
    music = Music.objects.all() 
    serializer = MusicSerializer(music, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_song(request, id):
    try:
        song = Music.objects.get(id=id) 
    except Music.DoesNotExist:
        return Response('нет такой песни') 

    serializer = MusicSerializer(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def post_music(request):
    # print(request.data)
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)









# DELETE, PUT, PATCH   
# @api_view(['PUT', ''PATCH]) 