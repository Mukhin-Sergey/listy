from django.contrib import admin
from .models import User
from listy.admin import admin_site

@admin.register(User, site=admin_site)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'date_joined',)  # Поля для отображения
    search_fields = ('nickname',)  # Поля для поиска