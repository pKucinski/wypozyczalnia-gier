from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from main import views
from main.views import index, login_page, faq, orders, profile, logout_request, signup, profile, show_product, \
    show_basket, products_category, change_password, add_to_basket, remove_item_from_basket

from main.views import index, login_page, faq, orders, profile, logout_request, signup, profile, show_product, show_basket, change_password,show_search,send_Email


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_page),
    path('sendEmail/', send_Email,name='sendmailnow'),
    path('kategoria/<int:id>', products_category),
    url(r'^haslo/$', change_password, name="change_password"),
    path('koszyk/', show_basket),
    path('search/', show_search, name="search_game"),
    path('index/', add_to_basket, name="searchid"),
    path('basket/', remove_item_from_basket, name="deleteid"),
    path('faq/', faq),
    path('produkt/<int:id>/', show_product),
    path('zamowienia/', orders),
    path('profil/', profile, name='profileDetail'),
    path("registration/", signup, name="signup"),
    path("logout/", logout_request),
    path('', index, name='home'),


    path('djrichtextfield/', include('djrichtextfield.urls')),
]
