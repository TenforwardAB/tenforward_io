from django.db import models
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

from modelcluster.fields import ParentalKey


from streams import blocks as myblocks
from wagtail_svgmap.blocks import ImageMapBlock


class WritingsPage(RoutablePageMixin, Page):
	template = 'company/company_page.html'
	description = models.CharField(max_length=255, blank=True, )

	content_panels = Page.content_panels + [
		FieldPanel('description', classname="full")
	]

	def get_context(self, request, *args, **kwargs):
		context = super(WritingsPage, self).get_context(request, *args, **kwargs)
		context['posts'] = self.posts
		context['blog_page'] = self
		context['search_type'] = getattr(self, 'search_type', "")
		context['search_term'] = getattr(self, 'search_term', "")
		return context

	def get_posts(self):
		return PostPage.objects.descendant_of(self).live().order_by('-date')

	@route(r'^(\d{4})/$')
	@route(r'^(\d{4})/(\d{2})/$')
	@route(r'^(\d{4})/(\d{2})/(\d{2})/$')
	def post_by_date(self, request, year, month=None, day=None, *args, **kwargs):
		self.posts = self.get_posts().filter(date__year=year)
		self.search_type = 'date'
		self.search_term = year
		if month:
			self.posts = self.posts.filter(date__month=month)
			df = DateFormat(date(int(year), int(month), 1))
			self.search_term = df.format('F Y')
		if day:
			self.posts = self.posts.filter(date__day=day)
			self.search_term = date_format(date(int(year), int(month), int(day)))
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
	def post_by_date_slug(self, request, year, month, day, slug, *args, **kwargs):
		post_page = self.get_posts().filter(slug=slug).first()
		if not post_page:
			raise Http404
		return Page.serve(post_page, request, *args, **kwargs)

	@route(r'^tag/(?P<tag>[-\w]+)/$')
	def post_by_tag(self, request, tag, *args, **kwargs):
		self.search_type = 'tag'
		self.search_term = tag
		self.posts = self.get_posts().filter(tags__slug=tag)
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^category/(?P<category>[-\w]+)/$')
	def post_by_category(self, request, category, *args, **kwargs):
		self.search_type = 'category'
		self.search_term = category
		self.posts = self.get_posts().filter(categories__slug=category)
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^$')
	def post_list(self, request, *args, **kwargs):
		self.posts = self.get_posts()
		return Page.serve(self, request, *args, **kwargs)

	@route(r'^search/$')
	def post_search(self, request, *args, **kwargs):
		search_query = request.GET.get('q', None)
		self.posts = self.get_posts()
		if search_query:
			self.posts = self.posts.filter(body__contains=search_query)
			self.search_term = search_query
			self.search_type = 'search'
		return Page.serve(self, request, *args, **kwargs)


class WritingPostPage(Page):
	template = 'writings/writing_post_page.html'
	pass

class BlogPage(Page):
	template = 'writings/blog_page.html'
	pass


class NewsPage(Page):
	template = 'writings/news_page.html'
	pass

class ArticlePage(Page):
	template = 'writings/article_page.html'
	pass