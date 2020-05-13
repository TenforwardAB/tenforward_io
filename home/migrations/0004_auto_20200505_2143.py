# Generated by Django 3.0.6 on 2020-05-05 21:43

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200505_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('Image', wagtail.images.blocks.ImageChooserBlock()), ('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('fancy_richtext', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(label='Body', required=True)), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('two_columns_block', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('regular-width', 'Regular Width'), ('full-width', 'Full Width'), ('regular-width padded', 'Regular Width, Padded'), ('full-width padded', 'Full Width, Padded')])), ('left_column_width', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], help_text='Column width is represented as units out of twelve. EX. 6 / 12 units will take up half the container.')), ('fixed_height', wagtail.core.blocks.IntegerBlock(default=350, help_text='Blocks that contain images that are placed in one of the columns here will set themselves to this height unless specifically overridden on the block.', label='Suggested height for contained widgets')), ('gutter_width', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(0, 0), (12, 12), (20, 20), (30, 30), (40, 40)], help_text='This determines how wide the spacing between columns will be, in pixels.', label='Column Gutter Width (pixels)')), ('background', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False))])), ('left_column', wagtail.core.blocks.StreamBlock([('FancyRichTextBlock', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(label='Body', required=True)), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('CalloutBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('ImageCarouselBlock', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.TextBlock(required=False)), ('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))]))]))), ('cycle_timeout', wagtail.core.blocks.IntegerBlock(default=5000, help_text='The time between automatic image cycles (in milliseonds). Set to 0 to disable automatic cycling.'))])), ('ImageGalleryBlock', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('gallery', 'Image Gallery'), ('slider', 'Image Slider w/ Thumbnail Picker')])), ('columns', wagtail.core.blocks.ChoiceBlock(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (6, 6)])), ('height', wagtail.core.blocks.IntegerBlock(default=300, help_text="Images' widths will be scaled with the number of columns. This field determines their height.", label='Height (pixels)')), ('images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(label='Image')))])), ('RelatedLinksBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))]))], label='Link'), label='Links')), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('ImagePanelBlock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('link', 'Image Link'), ('captioned', 'Image w/ Caption'), ('rollover', 'Image Link w/ Rollover Text'), ('separate_text', 'Image Card (Equal Heights)'), ('separate_text_natural', 'Image Card (Natural Heights)'), ('image_listing_left', 'Listing (Image Left)'), ('image_listing_right', 'Listing (Image Right)')])), ('title', wagtail.core.blocks.CharBlock(required=False)), ('desc', wagtail.core.blocks.CharBlock(label='Body', required=False)), ('display_caption', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this box to display the caption and photo credit below this image.', label='Display Caption', required=False)), ('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('VideoBlock', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste the video URL from YouTube or Vimeo. e.g. https://www.youtube.com/watch?v=l3Pz_xQZVDg or https://vimeo.com/207076450.', label='Video Embed URL')), ('title', wagtail.core.blocks.CharBlock(required=False)), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('IFrameEmbedBlock', wagtail.core.blocks.StructBlock([('html', streams.blocks.IFrameBlock()), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('SectionTitleBlock', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('section_divider', 'Section Divider'), ('block_header', 'Block Header')], requried=True))])), ('MenuListingBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='If supplied, display this at the top of the menu listing', required=False)), ('show', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('siblings', 'Page Siblings'), ('children', 'Page Children')], help_text='"Page Siblings" lists all pages at the same level of the site page hierarchy as this page; "Page Children" lists all pages that are directly below this page in the page hierarchy.')), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('SpacerBlock', wagtail.core.blocks.StructBlock([('height', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(12, 12), (20, 20), (25, 25), (30, 30), (40, 40), (50, 50), (75, 75), (100, 100), (125, 125), (150, 150), (175, 175), (200, 200), (225, 225), (250, 250)], help_text='Add empty vertical space whose height is this many pixels.', label='Height (pixels)'))]))], icon='arrow-left', label='Left column content', required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('FancyRichTextBlock', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(label='Body', required=True)), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('CalloutBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('ImageCarouselBlock', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.TextBlock(required=False)), ('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))]))]))), ('cycle_timeout', wagtail.core.blocks.IntegerBlock(default=5000, help_text='The time between automatic image cycles (in milliseonds). Set to 0 to disable automatic cycling.'))])), ('ImageGalleryBlock', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('gallery', 'Image Gallery'), ('slider', 'Image Slider w/ Thumbnail Picker')])), ('columns', wagtail.core.blocks.ChoiceBlock(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (6, 6)])), ('height', wagtail.core.blocks.IntegerBlock(default=300, help_text="Images' widths will be scaled with the number of columns. This field determines their height.", label='Height (pixels)')), ('images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(label='Image')))])), ('RelatedLinksBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))]))], label='Link'), label='Links')), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('ImagePanelBlock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('link', 'Image Link'), ('captioned', 'Image w/ Caption'), ('rollover', 'Image Link w/ Rollover Text'), ('separate_text', 'Image Card (Equal Heights)'), ('separate_text_natural', 'Image Card (Natural Heights)'), ('image_listing_left', 'Listing (Image Left)'), ('image_listing_right', 'Listing (Image Right)')])), ('title', wagtail.core.blocks.CharBlock(required=False)), ('desc', wagtail.core.blocks.CharBlock(label='Body', required=False)), ('display_caption', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this box to display the caption and photo credit below this image.', label='Display Caption', required=False)), ('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('VideoBlock', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste the video URL from YouTube or Vimeo. e.g. https://www.youtube.com/watch?v=l3Pz_xQZVDg or https://vimeo.com/207076450.', label='Video Embed URL')), ('title', wagtail.core.blocks.CharBlock(required=False)), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('IFrameEmbedBlock', wagtail.core.blocks.StructBlock([('html', streams.blocks.IFrameBlock()), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('SectionTitleBlock', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('section_divider', 'Section Divider'), ('block_header', 'Block Header')], requried=True))])), ('MenuListingBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='If supplied, display this at the top of the menu listing', required=False)), ('show', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('siblings', 'Page Siblings'), ('children', 'Page Children')], help_text='"Page Siblings" lists all pages at the same level of the site page hierarchy as this page; "Page Children" lists all pages that are directly below this page in the page hierarchy.')), ('color', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='This image, if supplied, will appear as a background for this block', required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Transparent'), ('white', 'White'), ('black', 'Black'), ('orange', 'Orange'), ('ltgray', 'Light Gray'), ('midgray', 'Mid Gray'), ('darkergray', 'Dark Gray'), ('dkgray', 'Very Dark Gray'), ('olivegreen', 'Olive Green'), ('purple', 'Purple'), ('darkteal', 'Dark Teal')], help_text='Set the background color of this block.  If a Background Image is also supplied, the Background Image will be displayed instead of this color', required=False)), ('text_color', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(None, 'Default'), ('dkgray', 'Dark Gray'), ('black', 'Black'), ('white', 'White')], help_text='Set the color for the text in this block. This is here so you can make your text visible on both light and dark backgrounds.', required=False))])), ('fixed_dimensions', wagtail.core.blocks.StructBlock([('use', wagtail.core.blocks.BooleanBlock(default=False, help_text='Normally, the image will expand its height to satisfy the suggested height on its parent block. Checking this box will make it conform to the specified height and width, instead.', label='Use Fixed Dimensions', required=False)), ('height', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "layout), set the image to be this many pixels tall.', label='Height (pixels)')), ('width', wagtail.core.blocks.IntegerBlock(default=200, help_text='If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column layout), set the image to be this many pixels wide.', label='Width (pixels)'))]))])), ('SpacerBlock', wagtail.core.blocks.StructBlock([('height', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[(12, 12), (20, 20), (25, 25), (30, 30), (40, 40), (50, 50), (75, 75), (100, 100), (125, 125), (150, 150), (175, 175), (200, 200), (225, 225), (250, 250)], help_text='Add empty vertical space whose height is this many pixels.', label='Height (pixels)'))]))], icon='arrow-right', label='Right column content', required=False))])), ('integer_choice_block', wagtail.core.blocks.ChoiceBlock(choices=[])), ('link_block', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to the chosen page. If a Page is selected, it will take precedence over both.', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Link to the chosen document. If a document is selected, it will take precedence over a URL.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs must include the http:// otherwise they will not work.', required=False))]))], blank=True, null=True),
        ),
    ]
