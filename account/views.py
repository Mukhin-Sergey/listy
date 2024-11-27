# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registration.models import User
from upload.models import Track

def index(request):
    return render(request, 'account/index.html')

def account_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user:
            return render(request, 'account/index.html', {'user': user})
    return render(request, 'account/index.html', {'message': 'Вы не вошли в аккаунт.'})

def delete_view(request, track_id):
    user_id = request.session.get('user_id')
    
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user:
            # Проверяем, существует ли трек, связанный с этим пользователем
            track = Track.objects.filter(id=track_id, user=user).first()
            if track:
                track.delete()  # Удаляем трек из базы данных
                return redirect('/account/')  # Перенаправляем на личный кабинет
            else:
                return HttpResponse("Трек не найден", status=404)
    
    return redirect('/registration/')  # Если пользователь не авторизован, перенаправляем на страницу регистрации

# Выход
def logout_view(request):
    request.session.flush()
    return redirect('/account/')
