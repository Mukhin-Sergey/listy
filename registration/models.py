from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
