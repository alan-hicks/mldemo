#----------------------------------------------------------------------
# Copyright (c) 2014-2016, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
multi lingual demo site
"""

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls import i18n as django_conf_urls_i18n

from mldemo import views
from filebrowser.sites import site
from mezzanine.generic.views import admin_keywords_submit
from mezzanine.pages.views import admin_page_ordering, page
from mezzanine.core.views import edit, search, set_site, set_device, static_proxy, displayable_links_js

urlpatterns = [
    # redirect/home
    url('^redirect/(?P<typeofpage>.*)$', views.redirect_pagetype,
        name='redirect_pagetype'),
    url(r'^i18n/', include(django_conf_urls_i18n)),
]
urlpatterns += [
    url("^admin_keywords_submit/$", admin_keywords_submit,
        name="admin_keywords_submit"),
]
urlpatterns += i18n_patterns(
    # Home page for each language
    url(r"^$", views.home, name="home"),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Filebrowser
    url(r'^admin/filebrowser/', include(site.urls)),
)
urlpatterns += i18n_patterns(
    # Mezzanine url's
    url("^admin_page_ordering/$", admin_page_ordering, name="admin_page_ordering"),
)
urlpatterns += i18n_patterns(
    # Mezzanine url's
    url("^edit/$", edit, name="edit"),
    url("^search/$", search, name="search"),
    url("^set_site/$", set_site, name="set_site"),
    url("^set_device/(?P<device>.*)/$", set_device, name="set_device"),
    url("^asset_proxy/$", static_proxy, name="static_proxy"),
    url("^displayable_links.js$", displayable_links_js,
        name="displayable_links_js"),
)
urlpatterns += i18n_patterns(
    # Catchall with site-id fixing for language
    url("^(?P<slug>.*)%s$" % ("/" if settings.APPEND_SLASH else ""),
        page, name="page"),
)

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
