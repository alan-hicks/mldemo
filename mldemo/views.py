#----------------------------------------------------------------------
# Copyright (c) 2014-2022, Persistent Objects Ltd https://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
multi lingual demo site
"""

import sys
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.utils import translation

from mldemo.models import Mlpage, Pagetype
from mezzanine.pages.models import Page

def redirect_pagetype(request, typeofpage):
    """
    Used to redirect to a page for a different language
    e.g. from English language about us page to French version
    Request: redirect/aboutus
    Response fr/about-us
    """

    ret = '/'

    # set session site_id according to sites/language
    cur_language = translation.get_language()
    try:
        sid = settings.LANGUAGE_SITE_MAP[cur_language]
        setattr(request, "site_id", sid)
        request.session["site_id"] = sid
    except KeyError:
        msg = 'Please add language %s to settings.LANGUAGE_SITE_MAP' % cur_language
        sys.stderr.write(msg + '\n')
        sys.stderr.flush()

    # Find the pagetype (home, aboutus, etc.)
    try:
        #pylint: disable=no-member
        ptype = Pagetype.objects.get(title=typeofpage)
        pid = Mlpage.objects.get(pagetype=ptype.id)
        thispage = Page.objects.get(id=pid.page_ptr_id, status=2)
        if thispage.slug != '/':
            ret = '/' + thispage.slug
    except ObjectDoesNotExist:
        # Pagetype not found
        pass
    except:
        sys.stderr.write('redirect_pagetype: ' + typeofpage + '\n')

    # redirect to the home page or the found page
    return HttpResponseRedirect(ret)

def home(request):
    """
    Home page request
    """
    filter_page = (
        'audience',
        'you',
        'marketing',
    )
    fp_pages = Page.objects.filter(
        content_model='mlpage',
        mlpage__pagetype__title__in=filter_page).order_by('_order')
    thispage = Page.objects.get(slug='/')
    sql = '''SELECT s.domain, pp.slug,
    substr(s.domain, 1 + position('/' IN s.domain)) as language_code
    FROM   mldemo_mlpage AS p
    INNER JOIN mldemo_pagetype AS t ON p.pagetype_id = t.id
    INNER JOIN pages_page AS pp ON pp.id = p.page_ptr_id
    INNER JOIN django_site AS s ON pp.site_id = s.id
    WHERE t.title = %s'''
    if thispage.mlpage.pagetype:
        cursor = connection.cursor()
        cursor.execute(sql, [thispage.mlpage.pagetype.title])
        hreflang_list = cursor.fetchall()
    else:
        hreflang_list = {}

    context = {
        'languages': settings.LANGUAGES,
        'hreflang_list': hreflang_list,
        "fp_pages": fp_pages,
        "page": thispage,
    }
    return render(request, 'mldemo/home.html', context)
