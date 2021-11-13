from django.db import models
from cloudinary.models import CloudinaryField


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    amount = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    buy_counter = models.DecimalField(max_digits=6, decimal_places=0, default=0, editable=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title
