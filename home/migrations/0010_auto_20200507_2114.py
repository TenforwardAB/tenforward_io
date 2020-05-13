# Generated by Django 3.0.6 on 2020-05-07 21:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200507_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('image_slider', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('slide', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image dimension needs to be XXXXX', required=False))]))])))]))], blank=True, null=True),
        ),
    ]
