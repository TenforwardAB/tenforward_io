from django.db import models
from django import forms
from django.http import Http404, HttpResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format

import datetime
from datetime import date

from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         StreamFieldPanel, InlinePanel)

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.blocks import RawHTMLBlock, BlockQuoteBlock, RichTextBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import StructBlock, RichTextBlock, CharBlock, StreamBlock

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalManyToManyField, ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase

from streams import blocks as myblocks
from wagtail_svgmap.blocks import ImageMapBlock


@register_snippet
class WritingCategory(models.Model):
	"""
	Categories for the Writings (IE. Blog/News/Article)
	"""
	name = models.CharField(max_length=100)
	slug = models.SlugField(
		verbose_name='slug',
		allow_unicode=True,
		max_length=100
	)

	panels =[
		FieldPanel("name"),
		FieldPanel("slug")
	]

	class Meta:
		verbose_name = "Writing Category"
		verbose_name = "Writing Categories"
		ordering = ["name"]

	def __str__(self):
		return self.name


class WritingPageTag(TaggedItemBase):
	content_object = ParentalKey(
		'WritingPostPage',
		related_name='tagged_items',
		on_delete=models.CASCADE,
	)


@register_snippet
class Tag(TaggitTag):
	class Meta:
		proxy = True


class WritingsPage(RoutablePageMixin, Page):
	template = 'writings/writings_page.html'

	description = models.CharField(max_length=255, blank=True, )

	content_panels = Page.content_panels + [
		FieldPanel('description', classname="full")
	]

	def get_context(self, request, *args, **kwargs):
		context = super(WritingsPage, self).get_context(request, *args, **kwargs)
		context['writings'] = self.writings
		context['writing_page'] = self
		context['writing_types'] = WritingCategory.objects.all()
		context['search_type'] = getattr(self, 'search_type', "")
		context['search_term'] = getattr(self, 'search_term', "")
		return context

	def get_writings(self):
		return WritingPostPage.objects.descendant_of(self).live().order_by('-date')

	@property
	def articles(self):
		return self.get_writings().filter(writing_categories__slug='writing_categories')

	@route(r'^(\d{4})/$')
	@route(r'^(\d{4})/(\d{2})/$')
	@route(r'^(\d{4})/(\d{2})/(\d{2})/$')
	def writing_by_date(self, request, year, month=None, day=None, *args, **kwargs):
		self.writings = self.get_writings().filter(date__year=year)
		self.search_type = 'date'
		self.search_term = year
		if month:
			self.writings = self.writings.filter(date__month=month)
			df = DateFormat(date(int(year), int(month), 1))
			self.search_term = df.format('F Y')
		if day:
			self.writings = self.writings.filter(date__day=day)
			self.search_term = date_format(date(int(year), int(month), int(day)))
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
	def writing_by_date_slug(self, request, year, month, day, slug, *args, **kwargs):
		post_page = self.get_writings().filter(slug=slug).first()
		if not post_page:
			raise Http404
		return Page.serve(post_page, request, *args, **kwargs)

	@route(r'^tag/(?P<tag>[-\w]+)/$')
	def writing_by_tag(self, request, tag, *args, **kwargs):
		self.search_type = 'tag'
		self.search_term = tag
		self.writings = self.get_writings().filter(tags__slug=tag)
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^category/(?P<writingcategory>[-\w]+)/$')
	def writing_by_category(self, request, writingcategory, *args, **kwargs):
		print('KKKKKKK')
		self.search_type = 'category'
		self.search_term = writingcategory
		self.writings = self.get_writings().filter(writing_categories__slug=writingcategory)
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^(.+)/$')
	def writing_by_slug(self, request, slug, *args, **kwargs):
		post_page = self.get_writings().filter(slug=slug).first()
		if not post_page:
			raise Http404
		return Page.serve(post_page, request, *args, **kwargs)

	@route(r'^search/$')
	def writing_search(self, request, *args, **kwargs):
		search_query = request.GET.get('q', None)
		self.writings = self.get_writings()
		if search_query:
			self.writings = self.writings.filter(body__contains=search_query)
			self.search_term = search_query
			self.search_type = 'search'
		return Page.serve(self, request, *args, **kwargs)


	@route(r'^$')
	def writing_list(self, request, *args, **kwargs):
		self.writings = self.get_writings()
		search_query = request.GET.get('q', None)
		if search_query:
			self.writings = self.writings.filter(body__contains=search_query)
			self.search_term = search_query
			self.search_type = 'search'
		return Page.serve(self, request, *args, **kwargs)




class WritingPostPage(Page):
	template = 'writings/writing_post_page.html'


	body = RichTextField(blank=True)
	date = models.DateTimeField(verbose_name="Post date", default=datetime.datetime.today)

	excerpt = RichTextField(
		verbose_name='excerpt', blank=True, max_length=1000,
	)

	header_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
	)
	video_url = models.CharField(blank=True, null=True, max_length=255)
	video_thumb = models.ForeignKey(
		'wagtailimages.Image',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
	)

	writing_categories = ParentalManyToManyField("writings.WritingCategory", blank=False)
	tags = ClusterTaggableManager(through="writings.WritingPageTag", blank=True)

	content_panels = Page.content_panels + [
		ImageChooserPanel('header_image'),
		ImageChooserPanel('video_thumb'),
		FieldPanel("video_url"),
		FieldPanel("body"),
		FieldPanel("excerpt"),

		MultiFieldPanel(
			[
				FieldPanel("writing_categories",  widget=forms.CheckboxSelectMultiple)
			],
			heading="Writing Types"
		),
		FieldPanel("tags")
	]

	settings_panels = Page.settings_panels + [
		FieldPanel('date'),
	]

	@property
	def writing_page(self):
		return self.get_parent().specific

	def get_context(self, request, *args, **kwargs):
		context = super(WritingPostPage, self).get_context(request, *args, **kwargs)
		context['writing_page'] = self.writing_page
		context['writing'] = self
		return context


class BlogPage(Page):
	template = 'writings/blog_page.html'
	pass


class NewsPage(Page):
	template = 'writings/news_page.html'
	pass

class ArticlePage(Page):
	template = 'writings/article_page.html'
	pass