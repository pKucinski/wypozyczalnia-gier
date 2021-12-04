
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.db.models import Sum
from . import form
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Product, Categories, Basket, Rating


def index(request):
    products = Product.objects.all().order_by("-id")
    return render(request, 'index.html', {'products': products})






def login_page(request):
    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html/', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'haslo.html', {
        'form': form
    })


def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')


def faq(request):
    return render(request, 'faq.html')

def koszyk(request):
    return render(request, 'koszyk.html')


def products_category(request, id):
    category = get_object_or_404(Categories, pk=id)
    products = Product.objects.all
    return render(request, 'kategoria.html', {"category": category, "products": products})


def show_product(request, id):
    show_product = get_object_or_404(Product, pk=id)
    rating = Rating.objects.all()

    amount = show_product.amount
    if amount == 0:
        text = False
    elif amount == 1:
        text = "Została ostatnia sztuka!"
    elif amount > 1:
        text = "Dostępne " + str(show_product.amount) + " szt."

    show_product.amount = text

    return render(request, 'produkt.html', {'show_product': show_product, "rating": rating})


def show_basket(request):
    show_basket = Basket.objects.all().order_by("id")
    return render(request, 'koszyk.html', {'show_basket': show_basket})



@login_required
def password_view(request):
    return render(request, 'haslo.html')

@login_required
def orders(request):
    return render(request, 'zamowienia.html')


@login_required
def profile(request):
    userDetails = UserProfile.objects.filter(user__username=request.user)
    return render(request, 'profil.html', {'userDetails': userDetails})

