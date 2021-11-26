from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50)
    numberOfHouse = models.CharField(max_length=10)
    postCode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
          return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

    post_save.connect(create_user_profile, sender=User)


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