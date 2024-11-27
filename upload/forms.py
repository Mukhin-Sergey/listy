from django import forms
from .models import Track

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'song_file', 'cover_image']  # Поле artist необязательно
        labels = {
            'title': 'Название трека',
            'song_file': 'Файл с песней',
            'cover_image': 'Обложка трека',
        }
