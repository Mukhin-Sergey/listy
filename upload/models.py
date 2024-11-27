from django.db import models
from registration.models import User  # Импортируем модель User, чтобы связать с пользователем

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    song_file = models.FileField(upload_to='tracks/')
    cover_image = models.ImageField(upload_to='covers/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracks')
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления трека

    def save(self, *args, **kwargs):
        if not self.artist:  # Если поле artist не заполнено
            self.artist = self.user.nickname  # Заполняем его никнеймом пользователя
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.artist}"
