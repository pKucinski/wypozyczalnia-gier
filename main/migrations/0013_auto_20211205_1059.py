# Generated by Django 3.2.9 on 2021-12-05 10:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20211205_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
        migrations.AddField(
            model_name='basket',
            name='courses',
            field=models.ManyToManyField(related_name='xd', to=settings.AUTH_USER_MODEL),
        ),
    ]
