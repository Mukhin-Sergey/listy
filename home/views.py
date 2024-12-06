from django.shortcuts import render, get_object_or_404, redirect
from upload.models import Track
from registration.models import User
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    search_query = request.GET.get('q', '')  # Получаем параметр поиска из URL (если он есть)
    tracks = Track.objects.all()

    if search_query:
        tracks = tracks.filter(
            Q(title__icontains=search_query) | Q(artist__icontains=search_query)  # Поиск по названию и автору
        )

    paginator = Paginator(tracks, 3)  # Пагинация: 3 трека на страницу
    page_number = request.GET.get('page')  # Номер текущей страницы из URL
    page_obj = paginator.get_page(page_number)  # Получаем текущую страницу

    # Получаем текущего пользователя из сессии
    user_id = request.session.get('user_id')
    is_admin = False
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user and user.nickname == 'admin':  # Проверяем, администратор ли текущий пользователь
            is_admin = True

    return render(request, 'home/index.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'is_admin': is_admin,
    })


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Убираем защиту CSRF, если это тестовый проект (не рекомендуется для продакшена)
def delete_track(request, track_id):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user and user.nickname == 'admin':  # Только администратор может удалять
            track = get_object_or_404(Track, id=track_id)
            track.delete()
            return redirect('/')
    return redirect('/')  # Возврат на главную страницу



from django.contrib import messages

def edit_track(request, track_id):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user and user.nickname == 'admin':  # Только администратор может редактировать
            track = get_object_or_404(Track, id=track_id)
            if request.method == 'POST':
                new_title = request.POST['title']
                new_artist = request.POST['artist']

                # Проверяем, существует ли пользователь с таким именем
                if not User.objects.filter(nickname=new_artist).exists():
                    messages.error(request, f"Пользователя с никнеймом '{new_artist}' не существует.")
                    return render(request, 'home/edit_track.html', {'track': track})

                # Если всё корректно, сохраняем изменения
                track.title = new_title
                track.artist = new_artist
                track.user_id = User.objects.filter(nickname=new_artist).first()
                track.save()
                messages.success(request, 'Трек успешно обновлён.')
                return redirect('/')
            return render(request, 'home/edit_track.html', {'track': track})
    return redirect('/')  # Возврат на главную страницу

