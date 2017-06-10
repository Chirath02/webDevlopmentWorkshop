from django.conf.urls import url
from music.views import AlbumListView, AlbumCreateView, AlbumDetailView, AlbumDeleteView, AlbumUpdateView

urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name="album_list"),
    url(r'^add/$', AlbumCreateView.as_view(), name="album_create"),
    url(r'^(?P<pk>[0-9]+)/$', AlbumDetailView.as_view(), name="album_detail"),
    url(r'^(?P<pk>[0-9]+)/delete$', AlbumDeleteView.as_view(), name="album_delete"),
    url(r'^(?P<pk>[0-9]+)/update$', AlbumUpdateView.as_view(), name="album_update"),
]
