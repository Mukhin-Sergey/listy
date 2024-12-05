from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from upload.models import Track

def index(request):
    # Получаем параметр поиска
    search_query = request.GET.get('q', '')  # Параметр `q` из URL

    # Фильтрация треков
    if search_query:
        tracks = Track.objects.filter(
            Q(title__icontains=search_query) | Q(artist__icontains=search_query)  # Поиск по названию и артисту
        )
    else:
        tracks = Track.objects.all()  # Если нет параметра поиска, отображаем все треки

    # Настройка пагинации (по 3 трека на страницу)
    paginator = Paginator(tracks, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Передаем данные в шаблон
    return render(request, 'home/index.html', {'page_obj': page_obj, 'search_query': search_query})
