from django.shortcuts import render, HttpResponseRedirect
# from authapp.forms import ShopUserLoginForm
# from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse
# from .models import ShopUser


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
    return HttpResponseRedirect(reverse('main'))


def edit(request):
    return HttpResponseRedirect(reverse('main'))
