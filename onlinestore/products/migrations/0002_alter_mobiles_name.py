# Generated by Django 4.1.2 on 2022-10-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
