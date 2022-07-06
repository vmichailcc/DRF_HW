# Generated by Django 4.0.4 on 2022-07-05 16:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='description',
            field=models.TextField(max_length=800, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='store',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]