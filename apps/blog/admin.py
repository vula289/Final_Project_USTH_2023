# -*- coding: utf-8 -*-

from apps.blog.admins import (
    admin, DefaultAdminMixin,
    TagAdmin, PostAdmin, PageAdmin,
    VisitorAdmin, FavoriteAdmin
)

__all__ = (
    'admin',
    'DefaultAdminMixin',

    'TagAdmin',
    'PostAdmin',
    'PageAdmin',
    'VisitorAdmin',
    'FavoriteAdmin',
)
