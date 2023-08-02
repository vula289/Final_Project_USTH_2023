# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import (get_object_or_404, redirect)
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (TemplateView, FormView)

from apps.blog.models.post import Page
from apps.blog.forms.martor import MartorDemoForm


class BasePageDetailView(TemplateView):
    """ base class to show the detail of page """
    template_name = 'apps/blog/page/detail.html'
    content_path = None
    page_title = None

    def get_content(self):
        """ function to read the markdown content """
        file_path = os.path.join(settings.BASE_DIR, self.content_path)
        if os.path.exists(file_path):
            return open(file_path, 'r').read()
        return ''

    @property
    def extra_context(self):
        """ additional `context_data` for `get_context_data` """
        return None

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['page_title'] = self.page_title
        context_data['content'] = self.get_content()
        if self.extra_context:
            context_data.update(**self.extra_context)
        return context_data


class PageFromDatabaseView(BasePageDetailView):

    def get_object(self):
        slug = self.kwargs['slug']
        self.object = get_object_or_404(Page, slug=slug)
        self.page_title = self.object.title
        return self.object

    def get_content(self):
        return self.object.description

    @property
    def extra_context(self):
        """ additional `context_data` for `get_context_data` """
        return {'page': self.object}


class MartorDemoView(FormView):
    template_name = 'apps/blog/page/martor_demo.html'
    form_class = MartorDemoForm
