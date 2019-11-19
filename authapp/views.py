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
    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = ShopUserRegisterForm()

    return render(request, 'authapp/register.html', {'form': form})


def edit(request):
    return HttpResponseRedirect(reverse('main'))
