from django.contrib import admin
from .models import Categories, Product, UserProfile, Basket

# Register your models here.
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Basket)