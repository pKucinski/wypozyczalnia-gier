from django.contrib import admin
from django.urls import path
from main.views import index, login, faq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('faq/', faq),
    path('', index)
]
