# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from music.forms import SongModelForm
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
        form = SongModelForm()
        context["songs"] = songs
        context['form'] = form
        return context

    def post(self, request, **kwargs):
        form = SongModelForm(request.POST)
        form.album = Album.objects.get(id=self.kwargs['pk'])
        print form
        if form.is_valid():
            form.save()
            return redirect('album_detail', form.album.id)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(request, self.get_template_names(), context)


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


