from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from main import views
from main.views import index, login_page, faq, orders, profile, logout_request, signup, profile, show_product, \
    show_basket, products_category, change_password

from main.views import index, login_page, faq, orders, profile, logout_request, signup, profile, show_product, show_basket, add_to_basket, change_password,show_search,send_Email


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_page),
    path('sendEmail/', send_Email,name='sendmailnow'),
    path('kategoria/<int:id>', products_category),
    url(r'^haslo/$', change_password, name="change_password"),
    path('koszyk/', show_basket),
    path('search/', show_search, name="search_game"),
    path('faq/', faq),
    path('produkt/<int:id>/', show_product),
    path('zamowienia/', orders),
    path('profil/', profile, name='profileDetail'),
    path("registration/", signup, name="signup"),
    path("logout/", logout_request),
    path('', index),
    path('<str:productname>/', add_to_basket,name="insertproduct"),

    path('djrichtextfield/', include('djrichtextfield.urls')),
]
