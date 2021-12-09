# Generated by Django 3.2.9 on 2021-12-07 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0024_remove_basket_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddCart',
        ),
        migrations.DeleteModel(
            name='AddUserProfile',
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ManyToManyField(to='main.Product'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]