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


class CompanyPage(Page):
	template = 'company/company_page.html'
	pass


class ProductsPage(Page):
	template = 'company/products_page.html'
	pass


class ServicesPage(Page):
	template = 'company/services_page.html'
	pass

