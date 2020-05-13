from django.db import models

from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         StreamFieldPanel, InlinePanel)

from wagtail.core.models import Page
from wagtail.core.blocks import RawHTMLBlock, BlockQuoteBlock, RichTextBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import StructBlock, RichTextBlock, CharBlock, StreamBlock

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey


from streams import blocks as myblocks
from wagtail_svgmap.blocks import ImageMapBlock



class HomePage(Page):
    content = StreamField(
        [
            ('image_slider', myblocks.MainSliderBlock()),
            ('info_block1', myblocks.InfoBlock()),
            ('vertical_slide', myblocks.VerticalTabSlider()),
            ('pop_video', myblocks.VideoWithTextBlock()),
            ('client_block', myblocks.ClientBlock()),
            ('info_block2', myblocks.InfoBlock2()),
            ('faq_block', myblocks.FaqBlock())
        ],
        blank=True,
        null=True
    )
    # footer_text_long = models.TextField(max_length=2000)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]

    class Meta:  # noqa

        verbose_name = 'Home Page'
