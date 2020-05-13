# Generated by Django 3.0.6 on 2020-05-12 11:13

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20200511_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('image_slider', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('slide', wagtail.core.blocks.StructBlock([('bg_type', wagtail.core.blocks.ChoiceBlock(choices=[('bg-0', 'bg-0'), ('bg-1', 'bg-1'), ('bg-2', 'bg-2'), ('bg-3', 'bg-3'), ('bg-4', 'bg-4'), ('bg-5', 'bg-5'), ('bg-6', 'bg-6'), ('bg-7', 'bg-7'), ('bg-8', 'bg-8'), ('bg-9', 'bg-9'), ('bg-10', 'bg-10'), ('bg-11', 'bg-11'), ('bg-12', 'bg-12'), ('bg-13', 'bg-13'), ('bg-14', 'bg-14'), ('bg-15', 'bg-15'), ('bg-16', 'bg-16'), ('bg-17', 'bg-17'), ('bg-18', 'bg-18'), ('bg-19', 'bg-19'), ('bg-20', 'bg-20'), ('bg-rounded1', 'bg-rounded1'), ('bg-rounded2', 'bg-rounded2'), ('bg-rounded3', 'bg-rounded3'), ('bg-rounded4', 'bg-rounded4')], help_text='Set Slide BG according to docs')), ('text_placement', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'top'), ('left', 'left'), ('right', 'right')], help_text='Position of text on the slide')), ('heading', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image dimension needs to be XXXXX', required=False))]))])))])), ('info_block1', wagtail.core.blocks.StructBlock([('boxes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=400, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('/img/svg-icons/alarm', 'alarm'), ('/img/svg-icons/calendar', 'calendar'), ('/img/svg-icons/chat', 'chat'), ('/img/svg-icons/chat_multi', 'chat_multi'), ('/img/svg-icons/clock', 'clock'), ('/img/svg-icons/cloud-computing', 'cloud-computing'), ('/img/svg-icons/cup', 'cup'), ('/img/svg-icons/devices', 'devices'), ('/img/svg-icons/dial', 'dial'), ('/img/svg-icons/finger_tap', 'finger_tap'), ('/img/svg-icons/fingerprint', 'fingerprint'), ('/img/svg-icons/flag', 'flag'), ('/img/svg-icons/google-play', 'google-play'), ('/img/svg-icons/library', 'library'), ('/img/svg-icons/link', 'link'), ('/img/svg-icons/music', 'music'), ('/img/svg-icons/payment-method', 'payment-method'), ('/img/svg-icons/pictures', 'pictures'), ('/img/svg-icons/rocket', 'rocket'), ('/img/svg-icons/settings', 'settings'), ('/img/svg-icons/shirt', 'shirt'), ('/img/svg-icons/smartphones', 'smartphones')], help_text='Choose your')), ('url', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))], required=False))])))])), ('vertical_slide', wagtail.core.blocks.StructBlock([('tabs', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('top_mini_heading', wagtail.core.blocks.CharBlock(max_length=40, required=False)), ('major_heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('background', wagtail.core.blocks.ChoiceBlock(choices=[('bg-primary-color bg-5', 'blue'), ('bg-orange-light bg-6', 'orange'), ('bg-red bg-7', 'red')])), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear to the left of the text', required=False)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Text length have to be within 300-400 characters to fit image size', max_length=400, min_length=300, required=True))])))])), ('pop_video', wagtail.core.blocks.StructBlock([('video', wagtail.core.blocks.CharBlock(required=True)), ('video_thumb', wagtail.images.blocks.ImageChooserBlock(help_text='Thumbnail Image for the Video to be displayed, if not choosen default image will appear', required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('bg_type', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('bg-0', 'bg-0'), ('bg-1', 'bg-1'), ('bg-2', 'bg-2'), ('bg-3', 'bg-3'), ('bg-4', 'bg-4'), ('bg-5', 'bg-5'), ('bg-6', 'bg-6'), ('bg-7', 'bg-7'), ('bg-8', 'bg-8'), ('bg-9', 'bg-9'), ('bg-10', 'bg-10'), ('bg-11', 'bg-11'), ('bg-12', 'bg-12'), ('bg-13', 'bg-13'), ('bg-14', 'bg-14'), ('bg-15', 'bg-15'), ('bg-16', 'bg-16'), ('bg-17', 'bg-17'), ('bg-18', 'bg-18'), ('bg-19', 'bg-19'), ('bg-20', 'bg-20'), ('bg-rounded1', 'bg-rounded1'), ('bg-rounded2', 'bg-rounded2'), ('bg-rounded3', 'bg-rounded3'), ('bg-rounded4', 'bg-rounded4')])), ('text', wagtail.core.blocks.RichTextBlock(max_length=400, min_length=300, required=False))])), ('client_block', wagtail.core.blocks.StructBlock([('clients', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('logo_image', streams.blocks.TagFilterImageChooserBlock(required=True, tag='CLIENTLOGO')), ('url', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))], required=False))])))])), ('info_block2', wagtail.core.blocks.StructBlock([('mid_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'primary'), ('secondary', 'secondary'), ('gree', 'gree'), ('green-light', 'green-light'), ('black', 'black'), ('orange', 'orange'), ('orange-light', 'orange-light'), ('red', 'red'), ('grey', 'grey'), ('grey-light', 'grey-light'), ('yellow', 'yellow'), ('lime', 'lime')])), ('url', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))])), ('left_info_top', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=100, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('/img/svg-icons/alarm', 'alarm'), ('/img/svg-icons/calendar', 'calendar'), ('/img/svg-icons/chat', 'chat'), ('/img/svg-icons/chat_multi', 'chat_multi'), ('/img/svg-icons/clock', 'clock'), ('/img/svg-icons/cloud-computing', 'cloud-computing'), ('/img/svg-icons/cup', 'cup'), ('/img/svg-icons/devices', 'devices'), ('/img/svg-icons/dial', 'dial'), ('/img/svg-icons/finger_tap', 'finger_tap'), ('/img/svg-icons/fingerprint', 'fingerprint'), ('/img/svg-icons/flag', 'flag'), ('/img/svg-icons/google-play', 'google-play'), ('/img/svg-icons/library', 'library'), ('/img/svg-icons/link', 'link'), ('/img/svg-icons/music', 'music'), ('/img/svg-icons/payment-method', 'payment-method'), ('/img/svg-icons/pictures', 'pictures'), ('/img/svg-icons/rocket', 'rocket'), ('/img/svg-icons/settings', 'settings'), ('/img/svg-icons/shirt', 'shirt'), ('/img/svg-icons/smartphones', 'smartphones')], help_text='Choose your'))])), ('left_info_bottom', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=100, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('/img/svg-icons/alarm', 'alarm'), ('/img/svg-icons/calendar', 'calendar'), ('/img/svg-icons/chat', 'chat'), ('/img/svg-icons/chat_multi', 'chat_multi'), ('/img/svg-icons/clock', 'clock'), ('/img/svg-icons/cloud-computing', 'cloud-computing'), ('/img/svg-icons/cup', 'cup'), ('/img/svg-icons/devices', 'devices'), ('/img/svg-icons/dial', 'dial'), ('/img/svg-icons/finger_tap', 'finger_tap'), ('/img/svg-icons/fingerprint', 'fingerprint'), ('/img/svg-icons/flag', 'flag'), ('/img/svg-icons/google-play', 'google-play'), ('/img/svg-icons/library', 'library'), ('/img/svg-icons/link', 'link'), ('/img/svg-icons/music', 'music'), ('/img/svg-icons/payment-method', 'payment-method'), ('/img/svg-icons/pictures', 'pictures'), ('/img/svg-icons/rocket', 'rocket'), ('/img/svg-icons/settings', 'settings'), ('/img/svg-icons/shirt', 'shirt'), ('/img/svg-icons/smartphones', 'smartphones')], help_text='Choose your'))])), ('right_info_top', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=100, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('/img/svg-icons/alarm', 'alarm'), ('/img/svg-icons/calendar', 'calendar'), ('/img/svg-icons/chat', 'chat'), ('/img/svg-icons/chat_multi', 'chat_multi'), ('/img/svg-icons/clock', 'clock'), ('/img/svg-icons/cloud-computing', 'cloud-computing'), ('/img/svg-icons/cup', 'cup'), ('/img/svg-icons/devices', 'devices'), ('/img/svg-icons/dial', 'dial'), ('/img/svg-icons/finger_tap', 'finger_tap'), ('/img/svg-icons/fingerprint', 'fingerprint'), ('/img/svg-icons/flag', 'flag'), ('/img/svg-icons/google-play', 'google-play'), ('/img/svg-icons/library', 'library'), ('/img/svg-icons/link', 'link'), ('/img/svg-icons/music', 'music'), ('/img/svg-icons/payment-method', 'payment-method'), ('/img/svg-icons/pictures', 'pictures'), ('/img/svg-icons/rocket', 'rocket'), ('/img/svg-icons/settings', 'settings'), ('/img/svg-icons/shirt', 'shirt'), ('/img/svg-icons/smartphones', 'smartphones')], help_text='Choose your'))])), ('right_info_bottom', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=100, required=True)), ('svg_icon', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('/img/svg-icons/alarm', 'alarm'), ('/img/svg-icons/calendar', 'calendar'), ('/img/svg-icons/chat', 'chat'), ('/img/svg-icons/chat_multi', 'chat_multi'), ('/img/svg-icons/clock', 'clock'), ('/img/svg-icons/cloud-computing', 'cloud-computing'), ('/img/svg-icons/cup', 'cup'), ('/img/svg-icons/devices', 'devices'), ('/img/svg-icons/dial', 'dial'), ('/img/svg-icons/finger_tap', 'finger_tap'), ('/img/svg-icons/fingerprint', 'fingerprint'), ('/img/svg-icons/flag', 'flag'), ('/img/svg-icons/google-play', 'google-play'), ('/img/svg-icons/library', 'library'), ('/img/svg-icons/link', 'link'), ('/img/svg-icons/music', 'music'), ('/img/svg-icons/payment-method', 'payment-method'), ('/img/svg-icons/pictures', 'pictures'), ('/img/svg-icons/rocket', 'rocket'), ('/img/svg-icons/settings', 'settings'), ('/img/svg-icons/shirt', 'shirt'), ('/img/svg-icons/smartphones', 'smartphones')], help_text='Choose your'))]))]))], blank=True, null=True),
        ),
    ]