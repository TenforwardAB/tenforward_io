# Generated by Django 3.0.6 on 2020-05-08 09:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200508_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('image_slider', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('slide', wagtail.core.blocks.StructBlock([('bg_type', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('bg-0', 'bg-0'), ('bg-1', 'bg-1'), ('bg-2', 'bg-2'), ('bg-3', 'bg-3'), ('bg-4', 'bg-4'), ('bg-5', 'bg-5'), ('bg-6', 'bg-6'), ('bg-7', 'bg-7'), ('bg-8', 'bg-8'), ('bg-9', 'bg-9'), ('bg-10', 'bg-10'), ('bg-11', 'bg-11'), ('bg-12', 'bg-12'), ('bg-13', 'bg-13'), ('bg-14', 'bg-14'), ('bg-15', 'bg-15'), ('bg-16', 'bg-16'), ('bg-17', 'bg-17'), ('bg-18', 'bg-18'), ('bg-19', 'bg-19'), ('bg-20', 'bg-20'), ('bg-rounded1', 'bg-rounded1'), ('bg-rounded2', 'bg-rounded2'), ('bg-rounded3', 'bg-rounded3'), ('bg-rounded4', 'bg-rounded4')], help_text='Set Slide BG according to docs')), ('heading', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image dimension needs to be XXXXX', required=False))]))])))])), ('info_block1', wagtail.core.blocks.StructBlock([('boxes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=400, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('/img/svg-icons/alarm', 'alarm'), ('/img/svg-icons/calendar', 'calendar'), ('/img/svg-icons/chat', 'chat'), ('/img/svg-icons/chat_multi', 'chat_multi'), ('/img/svg-icons/clock', 'clock'), ('/img/svg-icons/cloud-computing', 'cloud-computing'), ('/img/svg-icons/cup', 'cup'), ('/img/svg-icons/devices', 'devices'), ('/img/svg-icons/dial', 'dial'), ('/img/svg-icons/finger_tap', 'finger_tap'), ('/img/svg-icons/fingerprint', 'fingerprint'), ('/img/svg-icons/flag', 'flag'), ('/img/svg-icons/google-play', 'google-play'), ('/img/svg-icons/library', 'library'), ('/img/svg-icons/link', 'link'), ('/img/svg-icons/music', 'music'), ('/img/svg-icons/payment-method', 'payment-method'), ('/img/svg-icons/pictures', 'pictures'), ('/img/svg-icons/rocket', 'rocket'), ('/img/svg-icons/settings', 'settings'), ('/img/svg-icons/shirt', 'shirt'), ('/img/svg-icons/smartphones', 'smartphones')], help_text='Choose your')), ('url', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))], required=False))])))]))], blank=True, null=True),
        ),
    ]
