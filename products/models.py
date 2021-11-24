from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

