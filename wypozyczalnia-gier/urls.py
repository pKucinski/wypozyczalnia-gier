from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from main import views
from main.views import index, login_page, faq, orders, profile, logout_request, signup, profile, show_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_page),

    path('faq/', faq),
    path('produkt/<int:id>/', show_product),
    path('zamowienia/', orders),
    path('profil/', profile, name='profileDetail'),
    path("registration/", signup, name="signup"),
    path("logout/", logout_request),
    path('', index),
    url(r'^haslo/$', views.change_password, name='change_password'),



]
