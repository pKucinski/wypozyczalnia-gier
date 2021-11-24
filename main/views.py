from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import  render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout



def index(request):
    return render(request, 'index.html')

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


def logout_request(request):
    logout(request)
    messages.info(request, 'Your password has been changed successfully!')
    return HttpResponseRedirect('/')


def faq(request):
    return render(request, 'faq.html')


def oders(request):
    return render(request, 'zamowienia.html')


def profile(request):
    return render(request, 'profil.html')





