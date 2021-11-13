from django.contrib import admin
from django.urls import path, include
from main.views import index, login, faq, oders, profile,registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login),
    path('registration/', registration),
    path('faq/', faq),
    path('zamowienia/', oders),
    path('profil/', profile),
    path('', index),



]
