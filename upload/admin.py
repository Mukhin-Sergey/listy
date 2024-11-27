from django.contrib import admin
from .models import Track
from listy.admin import admin_site  # Импортируем кастомный AdminSite
from django.utils.html import format_html


@admin.register(Track, site=admin_site)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'user', 'created_at', 'cover_preview',)  # Отображаемые поля
    search_fields = ('title', 'artist',)  # Поля для поиска
    list_filter = ('user',)  # Добавляем фильтры
    ordering = ('-created_at',)  # Сортировка
    date_hierarchy = 'created_at'  # Иерархия по дате
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.cover_image.url)
        return "Нет обложки"

    cover_preview.short_description = "Обложка"
