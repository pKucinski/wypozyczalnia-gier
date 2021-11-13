from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def login(request):
    return render(request, 'login.html')


def faq(request):
    return render(request, 'faq.html')


def oders(request):
    return render(request, 'zamowienia.html')


def profile(request):
    return render(request, 'profil.html')



