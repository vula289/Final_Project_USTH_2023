# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from updown.views import AddRatingFromModel

from apps.blog.models.post import Post
from apps.blog.feed import LatestPosts
from apps.blog.views.page import (
MartorDemoView
)
from apps.blog.views.post import (
    PostListView, PostListTaggedView,
    PostListAuthorView, PostListAuthorPrivateView,
    PostDetailView, PostCreateView, PostUpdateView,
    PostDeleteJSONView, PostMarkAsFeaturedJSONView
)
from apps.blog.views.tag import (
    TagListView, TagJSONSearchView,
    TagJSONCreateView
)
from apps.blog.views.addons import FavoriteCreateDeleteJSONView


app_name = 'apps.blog'

info_dict = {
    'queryset': Post.objects.published_public(),
    'date_field': 'updated_at'
}

urlpatterns = [
    # posts
    path('', PostListView.as_view(), name='post_list'),
    path('posts/me/', PostListAuthorPrivateView.as_view(), name='post_me'),
    path('posts/tagged/<slug:name>/', PostListTaggedView.as_view(), name='post_list_tagged'),
    path('posts/author/<slug:username>/', PostListAuthorView.as_view(), name='post_list_author'),
    path('posts/detail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/detail/<int:object_id>/rate/<str:score>', AddRatingFromModel(), {
        'app_label': 'blog',
        'model': 'Post',
        'field_name': 'rating'
    }, name='post_rating'),
    path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('posts/feed/', LatestPosts(), name='post_feed'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/json/', PostDeleteJSONView.as_view(), name='post_json_delete'),
    path('posts/mark-featured/<int:id>/', PostMarkAsFeaturedJSONView.as_view(), name='post_mark_featured'),

    # tags
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/search/json/', TagJSONSearchView.as_view(), name='tag_json_search'),
    path('tags/create/json/', TagJSONCreateView.as_view(), name='tag_json_create'),

    # addons
    path('favorite/json/', FavoriteCreateDeleteJSONView.as_view(), name='favorite_json_create_delete'),

     # pages
    path('try-martor-online/', MartorDemoView.as_view(), name='page_martor_demo')

]
