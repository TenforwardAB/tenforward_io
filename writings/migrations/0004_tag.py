# Generated by Django 3.0.6 on 2020-05-14 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('writings', '0003_auto_20200514_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('taggit.tag',),
        ),
    ]