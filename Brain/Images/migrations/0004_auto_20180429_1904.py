# Generated by Django 2.0.4 on 2018-04-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Images', '0003_auto_20180428_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
