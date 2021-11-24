from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    numberOfHouse = models.CharField(max_length=10)
    postCode = models.CharField(max_length=6)
    city = models.CharField(max_length=6)
