#----------------------------------------------------------------------
# Copyright (c) 1999-2014, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
multi lingual demo site
"""

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            settings.SITE_TITLE,
            column=1,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=(
                        'mldemo.models.Mlpage',
                    ),
                ),
            ]
        ))

        # append a group for "Administration"
        self.children.append(modules.Group(
            _('All pages'),
            column=1,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=(
                        'mezzanine.pages.*',
                        'mezzanine_blocks.*',
                        'mezzanine_bsbanners.*',
                    ),
                ),
            ]
        ))

        # append another link list module for "Media managment".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        # append a group for "Administration"
        self.children.append(modules.Group(
            _('Configuration'),
            column=2,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=(
                        'mezzanine_blocks.models.RichBlock',
                        'mezzanine_blocks.BlockCategory',
                        'mezzanine.conf.*',
                        'mldemo.models.Pagetype',
                        'mldemo.models.Typestatus',
                    ),
                ),
            ]
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Django: Administration'),
            column=2,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            collapsible=False,
            column=3,
        ))
