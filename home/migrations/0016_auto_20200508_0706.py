# Generated by Django 3.0.6 on 2020-05-08 07:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200508_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('image_slider', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('slide', wagtail.core.blocks.StructBlock([('bg_type', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('bg-0', 'bg-0'), ('bg-1', 'bg-1'), ('bg-2', 'bg-2'), ('bg-3', 'bg-3'), ('bg-4', 'bg-4'), ('bg-5', 'bg-5'), ('bg-6', 'bg-6'), ('bg-7', 'bg-7'), ('bg-8', 'bg-8'), ('bg-9', 'bg-9'), ('bg-10', 'bg-10'), ('bg-11', 'bg-11'), ('bg-12', 'bg-12'), ('bg-13', 'bg-13'), ('bg-14', 'bg-14'), ('bg-15', 'bg-15'), ('bg-16', 'bg-16'), ('bg-17', 'bg-17'), ('bg-18', 'bg-18'), ('bg-19', 'bg-19'), ('bg-20', 'bg-20'), ('bg-rounded1', 'bg-rounded1'), ('bg-rounded2', 'bg-rounded2'), ('bg-rounded3', 'bg-rounded3'), ('bg-rounded4', 'bg-rounded4')], help_text='Set Slide BG according to docs')), ('heading', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image dimension needs to be XXXXX', required=False))]))])))])), ('info_block1', wagtail.core.blocks.StructBlock([('box', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=400, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alarm', 'alarm'), ('calendar', 'calendar'), ('chat', 'chat'), ('chat_multi', 'chat_multi'), ('clock', 'clock'), ('cloud-computing', 'cloud-computing'), ('cup', 'cup'), ('devices', 'devices'), ('dial', 'dial'), ('finger_tap', 'finger_tap'), ('fingerprint', 'fingerprint'), ('flag', 'flag'), ('google-play', 'google-play'), ('library', 'library'), ('link', 'link'), ('music', 'music'), ('payment-method', 'payment-method'), ('pictures', 'pictures'), ('rocket', 'rocket'), ('settings', 'settings'), ('shirt', 'shirt'), ('smartphones', 'smartphones')], help_text='Choose your')), ('url', wagtail.core.blocks.URLBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
