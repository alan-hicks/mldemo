#----------------------------------------------------------------------
# Copyright (c) 2014-2019, Persistent Objects Ltd https://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
multi lingual demo site
"""

from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls import i18n as django_conf_urls_i18n
from django.urls import path


from mldemo import views
from filebrowser.sites import site
from mezzanine.generic.views import admin_keywords_submit
from mezzanine.pages.views import admin_page_ordering, page
from mezzanine.core.views import edit, search, set_site, static_proxy, displayable_links_js

urlpatterns = [
    # redirect/home
    path('redirect/<str:typeofpage>', views.redirect_pagetype,
        name='redirect_pagetype'),
    path('i18n/', include(django_conf_urls_i18n)),
]
urlpatterns += [
    path("admin_keywords_submit/", admin_keywords_submit,
        name="admin_keywords_submit"),
]
urlpatterns += i18n_patterns(
    # Home page for each language
    path("", views.home, name="home"),
    # Admin
    path('admin/', include(admin.site.urls)),
    # Filebrowser
    path('admin/filebrowser/', site.urls),
)
urlpatterns += i18n_patterns(
    # Mezzanine url's
    path("admin_page_ordering/", admin_page_ordering, name="admin_page_ordering"),
)
urlpatterns += i18n_patterns(
    # Mezzanine url's
    path("edit/", edit, name="edit"),
    path("search/", search, name="search"),
    path("set_site/", set_site, name="set_site"),
    path("asset_proxy/", static_proxy, name="static_proxy"),
    path("displayable_links.js", displayable_links_js,
        name="displayable_links_js"),
)
urlpatterns += i18n_patterns(
    # Catchall with site-id fixing for language
    path("<str:slug>", page, name="page"),
)

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
