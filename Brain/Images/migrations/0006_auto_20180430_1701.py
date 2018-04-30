# Generated by Django 2.0.4 on 2018-04-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Images', '0005_auto_20180429_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file_name',
            field=models.CharField(default='default.jpg', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
