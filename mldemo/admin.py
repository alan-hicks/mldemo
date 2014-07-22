#----------------------------------------------------------------------
# Copyright (c) 2014, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
Multilingual demo models
"""

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mldemo.models import Mlpage, Pagetype, Typestatus

class MlpageAdmin(PageAdmin):
    """
    Admin class for Mlpage
    """
    #pylint: disable=too-many-public-methods
    fieldsets = deepcopy(PageAdmin.fieldsets)

class PagetypeAdmin(admin.ModelAdmin):
    """
    Admin class for Pagetype
    """
    #pylint: disable=too-many-public-methods
    list_display = ('title', 'description', 'glyphicon', )

class TypestatusAdmin(admin.ModelAdmin):
    """
    Admin class for Typestatus
    Read only as this is a view of the translation status
    """
    #pylint: disable=too-many-public-methods
    actions = None
    readonly_fields = ['site_id', 'domain', 'type_id', 'title', 'pages']
    list_display = ('site_id', 'domain', 'type_id', 'title', 'pages')
    ordering = ['domain', 'title']

# Register your models here.
admin.site.register(Mlpage, PageAdmin)
admin.site.register(Pagetype, PagetypeAdmin)
admin.site.register(Typestatus, TypestatusAdmin)
