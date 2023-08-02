# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from allauth.account.models import (EmailAddress, EmailConfirmation)

from apps.blog.admins.admin import admin_site
from apps.blog.admins.base import DefaultAdminMixin
from apps.accounts.models.user import (User, Profile)


@admin.register(EmailAddress, site=admin_site)
class EmailAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailConfirmation, site=admin_site)
class EmailConfirmationAdmin(admin.ModelAdmin):
    pass


@admin.register(User, site=admin_site)
class UserAdmin(DefaultAdminMixin, admin.ModelAdmin):
    search_fields = ['username'] 
    pass


@admin.register(Profile, site=admin_site)
class ProfileAdmin(DefaultAdminMixin, admin.ModelAdmin):
    search_fields = ['display_name', 'user__username'] 
    pass
