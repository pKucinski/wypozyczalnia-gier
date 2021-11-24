 from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import  render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .models import Person


def index(request):
@ -35,15 +40,33 @@ def signup(request):
	return render(request, 'registration/registration.html/', {'form': form})


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
    messages.info(request, 'Your password has been changed successfully!')
    return HttpResponseRedirect('/')


def faq(request):
    return render(request, 'faq.html')

def haslo_view(request):
    return render(request, 'haslo.html')


def oders(request):
    return render(request, 'zamowienia.html')
@ -52,6 +75,10 @@ def oders(request):
def profile(request):
    return render(request, 'profil.html')

def profileDetail(request):
    userDetails=Person.objects.all()
    return render(request,'profil.html',{'userDetails':userDetails})
