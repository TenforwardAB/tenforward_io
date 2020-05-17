# -*- coding: utf-8 -*-
from django.template import Library, loader
from django.urls import resolve

import six

from ..models import WritingCategory as Category
from ..models import Tag

register = Library()


@register.simple_tag()
def writing_date_url(writing, writing_page):
    writing_date = writing.date
    url = writing_page.url + writing_page.reverse_subpage(
        'writing_by_date_slug',
        args=(
            writing_date.year,
            '{0:02}'.format(writing_date.month),
            '{0:02}'.format(writing_date.day),
            writing.slug,
        )
    )
    return url

@register.simple_tag()
def writing_date_url(writing, writing_page):
    writing_date = writing.date
    url = writing_page.url + writing_page.reverse_subpage(
        'writing_by_slug',
        args=(
            writing.slug,
        )
    )
    return url


@register.inclusion_tag('blog/components/tags_list.html', takes_context=True)
def tags_list(context, limit=None):
    writing_page = context['writing_page']
    tags = Tag.objects.all()
    if limit:
        tags = tags[:limit]
    return {'writing_page': writing_page, 'request': context['request'], 'tags': tags}


@register.inclusion_tag('blog/components/categories_list.html', takes_context=True)
def categories_list(context):
    writing_page = context['writing_page']
    categories = Category.objects.all()
    return {'writing_page': writing_page, 'request': context['request'], 'categories': categories}


@register.inclusion_tag('blog/components/writing_categories_list.html', takes_context=True)
def writing_categories(context):
    writing_page = context['writing_page']
    writing = context['writing']
    writing_categories = writing.categories.all()
    return {'writing_page': writing_page, 'writing_categories': writing_categories, 'request': context['request']}


@register.inclusion_tag('blog/components/writing_tags_list.html', takes_context=True)
def writing_tags_list(context):
    writing_page = context['writing_page']
    writing = context['writing']

    writing_tags = writing.tags.all()

    return {'writing_page': writing_page, 'request': context['request'], 'writing_tags': writing_tags}

@register.inclusion_tag('blog/components/writing_tags_list_vertical.html', takes_context=True)
def writing_tags_list_vertical(context):
    writing_page = context['writing_page']
    writing = context['writing']

    writing_tags = writing.tags.all()

    return {'writing_page': writing_page, 'request': context['request'], 'writing_tags': writing_tags}


@register.inclusion_tag('blog/comments/disqus.html', takes_context=True)
def show_comments(context):
    writing_page = context['writing_page']
    writing = context['writing']
    path = writing_date_url(writing, writing_page)

    raw_url = context['request'].get_raw_uri()
    parse_result = six.moves.urllib.parse.urlparse(raw_url)
    abs_path = six.moves.urllib.parse.urlunparse([
        parse_result.scheme,
        parse_result.netloc,
        path,
        "",
        "",
        ""
    ])

    return {'disqus_url': abs_path,
            'disqus_identifier': writing.pk,
            'request': context['request']}


@register.simple_tag(takes_context=True)
def canonical_url(context, writing=None):
    if writing and resolve(context.request.path_info).url_name == 'wagtail_serve':
        return context.request.build_absolute_uri(writing_date_url(writing, writing.writing_page))
    return context.request.build_absolute_uri()