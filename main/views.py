from django.contrib.auth import authenticate
from django.shortcuts import render, redirect




def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration/registration.html')


def faq(request):
    return render(request, 'faq.html')


def oders(request):
    return render(request, 'zamowienia.html')


def profile(request):
    return render(request, 'profil.html')