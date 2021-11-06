from django.contrib import admin
from django.urls import path
from main.views import index, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('', index)
]
