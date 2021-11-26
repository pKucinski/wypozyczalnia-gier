from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import UserProfile, Product, Categories

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
