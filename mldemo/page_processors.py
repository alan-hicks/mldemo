#----------------------------------------------------------------------
# Copyright (c) 2014-2016, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
Multilingual demo models
"""

from django.db import connection
from django.conf import settings
from mezzanine.pages.page_processors import processor_for
from mldemo.models import Mlpage

@processor_for(Mlpage)
def mlpage_languages(request, page):
    """
    Processor to add languages and settings
    """
    #pylint: disable=unused-argument
    canonical_url = page.slug
    sql = '''SELECT s.domain, pp.slug,
    substr(s.domain, 1 + position('/' IN s.domain)) as language_code
    FROM   mldemo_mlpage AS p
    INNER JOIN mldemo_pagetype AS t ON p.pagetype_id = t.id
    INNER JOIN pages_page AS pp ON pp.id = p.page_ptr_id
    INNER JOIN django_site AS s ON pp.site_id = s.id
    WHERE t.title = %s'''
    if page.mlpage.pagetype:
        cursor = connection.cursor()
        cursor.execute(sql, [page.mlpage.pagetype.title])
        hreflang_list = cursor.fetchall()
    else:
        hreflang_list = {}
    context = {
        'canonical_url': canonical_url,
        'hreflang_list': hreflang_list,
        'languages': settings.LANGUAGES,
        'site_title': settings.SITE_TITLE,
    }
    return context
