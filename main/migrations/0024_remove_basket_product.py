# Generated by Django 3.2.9 on 2021-12-05 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20211205_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='product',
        ),
    ]
