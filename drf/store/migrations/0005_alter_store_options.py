# Generated by Django 4.0.4 on 2022-07-11 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_store_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['-title']},
        ),
    ]