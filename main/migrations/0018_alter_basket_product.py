# Generated by Django 3.2.9 on 2021-12-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_basket_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ManyToManyField(blank=True, default=None, to='main.Product'),
        ),
    ]