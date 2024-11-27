# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TrackForm
from django.contrib.auth.decorators import login_required
from registration.models import User

def index(request):
    return render(request, 'upload/index.html')


def upload_view(request):
    user_id = request.session.get('user_id')  # Получаем ID пользователя из сессии
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user:
            if request.method == 'POST':
                form = TrackForm(request.POST, request.FILES)
                if form.is_valid():
                    track = form.save(commit=False)
                    track.user = user  # Привязываем трек к пользователю
                    track.save()
                    return redirect('/account/')  # Перенаправляем в личный кабинет после загрузки трека
            else:
                form = TrackForm()

            return render(request, 'upload/index.html', {'form': form})

    else:
        return redirect('/registration/')
