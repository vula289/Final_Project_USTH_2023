# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin
from django.contrib.auth.models import (User)
from django.contrib.auth.admin import (UserAdmin)
from django.utils.translation import ugettext_lazy as _

from apps.accounts.sites import AdminSite

admin_site = AdminSite()
admin_site.site_header = _('PySeeker')
admin_site.site_title = _('PySeeker')

admin.site = admin_site
admin.site.register(Site, SiteAdmin)
admin.site.register(User, UserAdmin)
