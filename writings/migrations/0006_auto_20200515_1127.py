# Generated by Django 3.0.6 on 2020-05-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0005_writingpostpage_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='writingpostpage',
            name='video',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='writingpostpage',
            name='video_thumb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
