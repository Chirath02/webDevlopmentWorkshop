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
        context['songs'] = Song.objects.filter(album=context['object'])
        context['form'] = SongModelForm()
        return context

    def post(self, request, **kwargs):
        form = SongModelForm(request.POST)
        if form.is_valid():
            album = self.get_object()
            Song(album=album, name=form.cleaned_data.get('name'), artist=form.cleaned_data.get('artist')).save()
            return redirect('album_detail', album.id)
        else:
            self.object = self.get_object()
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
    success_url = reverse_lazy('album_list')


class SongDetailView(DetailView):
    model = Song


class SongUpdateView(UpdateView):
    model = Song
    fields = ['name', 'artist']

    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.get_object().album.id})


class SongDeleteView(DeleteView):
    model = Song

    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.get_object().album.id})
