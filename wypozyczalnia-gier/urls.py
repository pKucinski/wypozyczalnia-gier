from django.contrib import admin
from django.urls import path, include

from main import views
from main.views import index, login_page, faq, oders, profile, logout_request, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_page),

    path('faq/', faq),
    path('zamowienia/', oders),
    path('profil/', profile),
    path("registration/", signup, name="signup"),
    path("logout/", logout_request),
    path('', index),



]
