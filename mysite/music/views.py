# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from music.models import Album, Song

# use class based views to implement all the views
# this will help to improve the security of your apps.


class AlbumListView(ListView):  # default template = album_list.html
    model = Album


class AlbumDetailView(DetailView):  # default template = album_detail.html
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        songs = Song.objects.filter(album=context['object'])
        context["songs"] = songs
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        artist = request.POST['artist']
        album = Album.objects.get(id=self.kwargs['pk'])
        song = Song(name=name, artist=artist, album=album)
        song.save()
        return redirect('album_detail', album.id)


class AlbumCreateView(CreateView):
    model = Album
    fields = ['name', 'img', 'genre']
    success_url = reverse_lazy('album_detail')


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['name', 'img', 'genre']
    success_url = reverse_lazy('album_detail')


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = '/music'


