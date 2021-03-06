from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from djrichtextfield.models import RichTextField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50)
    numberOfHouse = models.CharField(max_length=10)
    postCode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    phone = PhoneNumberField(null=False, blank=False, unique=False, max_length=9)

    def __str__(self):
          return "%s's profile" % self.user




class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
          return self.category_name



class Product(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = RichTextField(blank=False)
    age = models.DecimalField(max_digits=2, decimal_places=0, blank=False, default=3)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    amount = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    buy_counter = models.DecimalField(max_digits=6, decimal_places=0, default=0, editable=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):

        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, blank=False,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, blank=False,  on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False,default=0)

    def __str__(self):
        return "%s's basket" % self.id

