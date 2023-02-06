from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models  import Music
from music.serializers import MusicSerializer
from rest_framework import generics


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

@api_view(['DELETE'])
def delete_music(request, id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('нет такой песни!')
    song.delete()
    return Response('Successfully deleted!!')        


@api_view(['PUT', 'PATCH'])
def music_update(request, id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('Not such a song!!')    
    if request.method == 'PUT':
        serializer = MusicSerializer(instance=song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully updated!!')
    else: # PATCH
        serializer = MusicSerializer(instance=song, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('Successfully updated!!')   


# get запрос на классах
class MusicView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer 









# DELETE, PUT, PATCH   
# @api_view(['PUT', ''PATCH]) 