from django.contrib import admin
from django.urls import path
from main.views import index, login, faq, oders, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('faq/', faq),
    path('zamowienia/', oders),
    path('profil/', profile),
    path('', index)
]
