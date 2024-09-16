from django.shortcuts import render
from .models import Product, ProductCategory
import os

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


def index(request):
    context = {
        'title': 'Geekshop | Главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    #file_path = os.path.join(MODULE_DIR,'fixtures/products.json')
    context = {
        'title': 'Geekbrains | Каталог',
    }
    #context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)
