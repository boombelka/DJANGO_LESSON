from django.shortcuts import render
import json
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    context = {
        'title': 'Главная'

    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'ПРОДУКТЫ',
        'products': 'Product.objects.all()'}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contacts.html', context)


