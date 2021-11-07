from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def faq(request):
    return render(request, 'faq.html')


def oders(request):
    return render(request, 'zamowienia.html')


def profile(request):
    return render(request, 'profil.html')