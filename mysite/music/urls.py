from django.conf.urls import url
from music.views import *

urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name="album_list"),
    url(r'^add/$', AlbumCreateView.as_view(), name="album_create"),
    url(r'^(?P<pk>[0-9]+)/$', AlbumDetailView.as_view(), name="album_detail"),
    url(r'^(?P<pk>[0-9]+)/delete$', AlbumDeleteView.as_view(), name="album_delete"),
    url(r'^(?P<pk>[0-9]+)/update$', AlbumUpdateView.as_view(), name="album_update"),
    url(r'^song/(?P<pk>[0-9]+)/$', SongDetailView.as_view(), name="song_detail"),
    url(r'^song/(?P<pk>[0-9]+)/update$', SongUpdateView.as_view(), name="song_update"),
    url(r'^song/(?P<pk>[0-9]+)/delete$', SongDeleteView.as_view(), name="song_delete"),
]
