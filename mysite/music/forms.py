from django.forms import ModelForm
from music.models import Song


class SongModelForm(ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'name', 'artist']
