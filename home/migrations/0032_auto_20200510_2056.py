# Generated by Django 3.0.6 on 2020-05-10 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0031_auto_20200510_2051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Clients',
        ),
    ]
