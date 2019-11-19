from django.shortcuts import render, HttpResponseRedirect
# from authapp.forms import ShopUserLoginForm
# from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse
# from .models import ShopUser
from .forms import ShopUserRegisterForm  # подключение модуля для автоматизированных форм регистрации


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    return render(request, 'authapp/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    form = ShopUserRegisterForm()   # 1этап. приходит get запрос и мы создаем пустую форму
    if request.method == 'POST':   # 2 этап работа с уже заполненной формой
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid(): # 2.4 если форма неправильная то заполненая форма возвращается с ошибками.
            user = form.save()  # 2.2 заполнили форму и в базу данных внесли нового пользователя
            auth.login(request, user)    # 2.3. новоиспеченного юзера перенаправляем на главную страницу
            return HttpResponseRedirect(reverse('main'))
        form = ShopUserRegisterForm()

    return render(request, 'authapp/register.html', {'form': form})  # 1.1. форма пустая передается на регистрацию в register.html


def edit(request):
    return HttpResponseRedirect(reverse('main'))
