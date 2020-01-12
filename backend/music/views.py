from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from music.models import Song, Musician, Label
from music.serializers import SongListSerializer, SongFormSerializer, MusicianListSerializer, LabelListSerializer, \
    LabelFormSerializer, LabelNameSerializer, MusicianFormSerializer


#@swagger_auto_schema(method='GET', responses={200: SongListSerializer(many=True)})


@api_view(['GET'])
def song_list(request):
    songs = Song.objects.all()
    serializer = SongListSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def song_form_get(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist!'}, status=404)

    serializer = SongFormSerializer(song)
    return Response(serializer.data)

@api_view(['POST'])
def song_form_create(request):
    serializer = SongFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def song_form_update(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)
    serializer = SongFormSerializer(song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE', 'GET'])
def song_delete(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist'}, status=404)
    song.delete()
    return Response(status=204)

@api_view(['GET'])
def musician_list(request):
    musicians = Musician.objects.all()
    serializer = MusicianListSerializer(musicians, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def musician_create(request):
    serializer = MusicianListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def musician_form_get(request, pk):
    try:
        musician = Musician.objects.get(pk=pk);
    except Musician.DoesNotExist:
        return Response({'error': 'Musician does not exist'}, status=404)
    serializer = MusicianFormSerializer(musician)
    return Response(serializer.data)

@api_view(['PUT'])
def musician_form_update(request, pk):
    try:
        musician = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return Response({'error': 'Musician does not exist'}, status=404)
    serializer = MusicianFormSerializer(musician, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE', 'GET'])
def musician_delete(request, pk):
    try:
        musician = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return Response({'error': 'Musician does not exist'}, status=404)
    musician.delete()
    return Response(status=204)


@api_view(['GET'])
def label_list(request):
    labels = Label.objects.all()
    serializer = LabelListSerializer(labels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def label_form_create(request):
    serializer = LabelFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def label_form_get(request, pk):
    try:
        label = Label.objects.get(pk=pk);
    except Label.DoesNotExist:
        return Response({'error': 'Label does not exist'}, status=404)
    serializer = LabelFormSerializer(label)
    return Response(serializer.data)\

@api_view(['GET'])
def label_single_name_get(request, pk):
    try:
        label = Label.objects.get(pk=pk);
    except Label.DoesNotExist:
        return Response({'error': 'Label does not exist'}, status=404)
    serializer = LabelNameSerializer(label)
    return Response(serializer.data)

@api_view(['PUT'])
def label_form_update(request, pk):
    try:
        label = Label.objects.get(pk=pk)
    except Label.DoesNotExist:
        return Response({'error': 'Label does not exist'}, status=404)
    serializer = LabelFormSerializer(label, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE', 'GET'])
def label_delete(request, pk):
    try:
        label = Label.objects.get(pk=pk)
    except Label.DoesNotExist:
        return Response({'error': 'Label does not exist'}, status=404)
    label.delete()
    return Response(status=204)

