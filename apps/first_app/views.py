from django.shortcuts import render, HttpResponse, redirect
from apps.first_app.models import *

#SONGS

def songIndex(request): #same function as addSong
    all_songs = Song.objects.all()
    context = {
        "all_songs": all_songs
    }
    return render(request, "first_app/songIndex.html", context)

def add_song(request):
    if str(request.POST["form_button"]) == "pushed":
        Song.objects.create(title=request.POST["form_title"], description=request.POST["form_description"])

    return redirect("/")

def see_song(request, song_id):
    song = Song.objects.get(id= song_id)
    related_artists = song.artists.all()
    all_artists = Artist.objects.all()
    context = {
        "song": song,
        "related_artists": related_artists,
        "all_artists": all_artists,
    }
    return render(request, "first_app/song.html", context)

def add_artist_to_song(request, song_id):
    this_song = Song.objects.get(id=song_id)
    this_artist = Artist.objects.get(id=request.POST['artist'])
    this_song.artists.add(this_artist)

    return redirect("/songs/" + song_id)



#ARTISTS

def artistIndex(request):
    all_artists = Artist.objects.all()
    context = {
        "all_artists": all_artists
    }
    return render(request, "first_app/artistIndex.html", context)

def add_artist(request):
    if str(request.POST["form_button"]) == "pushed":
        Artist.objects.create(name=request.POST["form_name"], notes=request.POST["form_notes"])

    return redirect("/artists")

def see_artist(request, artist_id):
    artist = Artist.objects.get(id= artist_id)
    related_songs = artist.songs.all()
    all_songs = Song.objects.all()
    context = {
        "artist": artist,
        "related_songs": related_songs,
        "all_songs": all_songs,
    }
    return render(request, "first_app/artist.html", context)

def add_song_to_artist(request, artist_id):
    this_song = Song.objects.get(id=request.POST['song'])
    this_artist = Artist.objects.get(id=artist_id)
    this_artist.songs.add(this_song)

    return redirect("/artists/" + artist_id)