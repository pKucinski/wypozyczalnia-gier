# Generated by Django 3.2.8 on 2021-11-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_person_numberofhouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='numberOfHouse',
            field=models.CharField(max_length=10),
        ),
    ]
