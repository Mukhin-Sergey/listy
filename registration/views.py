# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def index(request):
    return render(request, 'registration/index.html')

# Страница регистрации и входа
def registration_view(request):
    if request.method == "POST":
        if 'register' in request.POST:
            # Регистрация
            nickname = request.POST['nickname']
            password = request.POST['password']
            if not User.objects.filter(nickname=nickname).exists():
                user = User.objects.create(nickname=nickname, password=password)
                user.save()
                # return redirect('/account/')
                return render(request, 'registration/index.html', {'success': 'Вы успешно зарегистрировались!'})
            else:
                return render(request, 'registration/index.html', {'error': 'Никнейм уже занят.'})
        elif 'login' in request.POST:
            # Вход
            nickname = request.POST['nickname']
            password = request.POST['password']
            user = User.objects.filter(nickname=nickname, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect('/account/')
            else:
                return render(request, 'registration/index.html', {'error': 'Неверный никнейм или пароль.'})
    return render(request, 'registration/index.html')
