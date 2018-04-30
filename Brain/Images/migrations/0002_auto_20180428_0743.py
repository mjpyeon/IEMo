# Generated by Django 2.0.4 on 2018-04-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/orig'),
        ),
    ]