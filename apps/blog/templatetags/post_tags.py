# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.db.models import Q

from apps.blog.models.tag import Tag
from apps.blog.models.post import Post
# from apps.blog.models.addons import Visitor

register = template.Library()


@register.simple_tag
def popular_tags(limit=5, query=None):
    """
    {% load post_tags %}
    {% popular_tags as popular_tags_list %}
    {% for tag in popular_tags_list %}
      <a href="{% url 'apps.blog:post_list_tagged' slug=tag.slug %}">
        {{ tag.slug }} <span class="badge">{{ tag.total }}</span>
      </a>
    {% endfor %}

    used in:
        - templates/apps/blog/post/list.html
    """
    if query:
        queryset = Tag.objects.published()\
                              .filter(Q(name__startswith=query))
    else:
        queryset = Tag.objects.published()

    maps = [
        {'tag': tag, 'total': tag.post_set.published_public().count()}
        for tag in queryset
    ]
    maps.sort(key=lambda x: x['total'], reverse=True)
    return maps[:limit]


@register.simple_tag
def random_posts(limit=5):
    """
    {% load post_tags %}
    {% random_posts as random_posts_list %}
    {% for post in random_posts_list %}
      <a href="{% url 'posts_detail' slug=post.slug %}">{{ post.title }}</a>
    {% endfor %}

    function to get the random posts.
    used in: templates/apps/blog/post/includes/sidebar_list.html
    """
    return Post.objects.published_public()\
                       .order_by('-rating_likes')\
                       .order_by('?')[:limit]


