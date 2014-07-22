#----------------------------------------------------------------------
# Copyright (c) 2014, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
multi lingual demo site
"""

from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin

from mldemo import views
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    # redirect/home
    url('^redirect/(?P<typeofpage>.*)$', views.redirect_pagetype,
        name='redirect_pagetype'),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
urlpatterns += patterns("mezzanine.generic.views",
    url("^admin_keywords_submit/$", "admin_keywords_submit",
        name="admin_keywords_submit"),
)
urlpatterns += i18n_patterns("",
    # Home page for each language
    url(r"^$", views.home, name="home"),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Filebrowser
    url(r'^admin/filebrowser/', include(site.urls)),
    # Grappelli
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
)
urlpatterns += i18n_patterns("mezzanine.pages.views",
    # Mezzanine url's
    url("^admin_page_ordering/$", "admin_page_ordering",
        name="admin_page_ordering"),
)
urlpatterns += i18n_patterns('mezzanine.core.views',
    # Mezzanine url's
    url("^edit/$", "edit", name="edit"),
    url("^search/$", "search", name="search"),
    url("^set_site/$", "set_site", name="set_site"),
    url("^set_device/(?P<device>.*)/$", "set_device", name="set_device"),
    url("^asset_proxy/$", "static_proxy", name="static_proxy"),
    url("^displayable_links.js$", "displayable_links_js",
        name="displayable_links_js"),
)
urlpatterns += i18n_patterns('mezzanine.pages.views',
    # Catchall with site-id fixing for language
    url("^(?P<slug>.*)%s$" % ("/" if settings.APPEND_SLASH else ""),
        "page", name="page"),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
