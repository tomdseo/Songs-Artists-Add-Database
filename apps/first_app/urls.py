from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.songIndex),
    url(r'^add_song$', views.add_song),
    url(r'^songs/(?P<song_id>\d+)', views.see_song),
    url(r'^artists$', views.artistIndex),
    url(r'^add_artist$', views.add_artist),
    url(r'^artists/(?P<artist_id>\d+)', views.see_artist),
    url(r'^add_artist_to_song/(?P<song_id>\d+)', views.add_artist_to_song),
    url(r'^add_song_to_artist/(?P<artist_id>\d+)', views.add_song_to_artist),
]