******
mldemo
******

Multilingual demo website with Python's Django and Mezzanine

Multilingual websites - I know my a-做

Summary
=======

The concept is simple, use the Django sites framework to manage each language and Mezzanine to manage the content.

Out of the box both Django and Mezzanine do site management, internationalization and localisation well.  What they don't do is mix them within a single site/application for a seamless multilingual experience. By creating a custom application using Mezzanine with a minor modification to allow multiple sites, the power of Django's Internationalization and Localisation framework are brought together with an easy to use cms application from Mezzanine to offer a well managed and intuitive multilingual website.

This multilingual website HOW-TO has been divided into five main aspects, Settings, Mezzanine patch, Models, Views and Templates.

Settings
========

The application needs to know what the available languages are, how they map to sites and what locales should be translated.  All these are part of settings.py.

The LANGUAGES list is a tuple of two tuples in the format (language code, language name)::

    # Available languages
    LANGUAGES = (
        ('en', _('English')),
        ('fr', _('French')),
        ('nl', _('Dutch')),
        ('es', _('Spanish')),
        ('zh-cn', _('Simplified Chinese')),
    )

Mapping languages to sites.  Although all the information may be available in the database, for efficiency this is extracted into a settings.LANGUAGE_SITE_MAP dictionary with the language code and the id from the django_sites table, in our example this is::

    # Mapping between Languages and Sites
    LANGUAGE_SITE_MAP = {
        'en': 1,
        'fr': 2,
        'es': 3,
        'nl': 4,
        'zh-cn': 5,
    }

As part of any Django multilingual application, the translations are identified by settings.LOCALE_PATHS, the Django documentation is an excellent resource for managing translations so won't be duplicated here.::

    # Location for the language translations
    LOCALE_PATHS = (
        (os.path.join(BASE_DIR, u'locale/zh-cn')),
        (os.path.join(BASE_DIR, u'locale/en')),
        (os.path.join(BASE_DIR, u'locale/es')),
        (os.path.join(BASE_DIR, u'locale/fr')),
        (os.path.join(BASE_DIR, u'locale/nl')),
    )

Mezzanine patch
===============

`See alan-hicks/mezzanine on Github <https://github.com/alan-hicks/mezzanine>`_

Models
======

The model class with information about the page types is Pagetype and only needs id, title and slug.  The description is for the convenience of the editors and translators and a useful focus when marketing for export.  As most of our new sites use Bootstrap it made sense to include a glyphicon to help visual identity.::

    class Pagetype(models.Model):
        """
        Page type used for joining pages and sites
        """
        GLYPHICON_CHOICES = (
            ('asterisk', 'glyphicon-asterisk'),
            ('plus', 'glyphicon-plus'),
        )
        title = models.CharField('Title', max_length=50)
        glyphicon = models.CharField('Icon', max_length=35, choices=GLYPHICON_CHOICES)
        description = models.CharField('Description', max_length=50)

        def __unicode__(self):
            return self.title

        class Meta(object):
            """
            Meta class for Pagetype
            """
            verbose_name = "Page type"
            verbose_name_plural = "Page types"
            ordering = ['title']

Our equivalent of the RichTextPage is Mlpage.

Although it would have been easy to add the single foreign key for the page type to the Mezzanine Page model, this would have complicated upgrading and so creating a new multilingual page à la RichText in our app should make future maintenance easier.::

    class Mlpage(Page, RichText):
        """
        Subclass of Mezzanine page adding page type
        """
        pagetype = models.ForeignKey(Pagetype, blank=True, null=True)

The way to extend Mezzanine tables and make any data available to a view is to add a Page Processor and our applications uses the following::

    @processor_for(Mlpage)
    def mlpage_languages(request, page):
        """
        Processor to add languages and settings
        """
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
            'hreflang_list': hreflang_list,
            'languages': settings.LANGUAGES,
            'site_title': settings.SITE_TITLE,
        }
        return context

Keeping track of translations is important and although the sql would be beyond the scope of the current orm, the model uses a view (managed = False) as though it were a table making it easy to view in Django's admin.::

    class Typestatus(models.Model):
        """
        Shows a matrix of sites and page types to help identify missing translations
        """
        site_id = models.IntegerField(primary_key=True)
        domain = models.CharField('domain', max_length=100)
        type_id = models.IntegerField()
        title = models.CharField('title', max_length=50)
        pages = models.IntegerField()

        def __unicode__(self):
            return self.domain + ' ' + self.title + ' ' + str(self.pages)

        class Meta(object):
            """
            Meta class for Typestatus
            """
            verbose_name = "Translation status"
            verbose_name_plural = "Translation status"
            managed = False
            ordering = ['domain', 'title']

The SQL for language coverage is standard SQL-92 and so should work on most modern databases, though as it joins two tables is not NoSQL friendly.::

    SELECT j.site_id, j.domain, j.type_id, j.title, count(p.id) pages
    FROM (
        SELECT p.id, p.site_id, mp.pagetype_id
        FROM pages_page p
        INNER JOIN mldemo_mlpage mp ON p.id = mp.page_ptr_id
        ) AS p
    RIGHT OUTER JOIN (
        SELECT s.id as site_id, s.domain, t.id as type_id, t.title
        FROM django_site s
        INNER JOIN mldemo_pagetype t ON TRUE) AS j
    ON p.site_id = j.site_id
    AND p.pagetype_id = j.type_id
    GROUP BY j.site_id, j.domain, j.type_id, j.title;

Views
=====

URLS
----

The URL dispatcher forwards requests to views. Although not complicated, urls are necessarily divided into those that do not use i18n and those that do.  The Django documentation has excellent information on its internationalization so only those aspects relating to our application are included here.

* urlpatterns += patterns
* urlpatterns += i18n_patterns

For example our redirect from one language to another ('^redirect/(?P<typeofpage>.*)$') and Django's ('^i18n/') are two that do not use i18n.::

    urlpatterns = patterns('',
        # redirect/home
        url('^redirect/(?P<typeofpage>.*)$', views.redirect_pagetype,
            name='redirect_pagetype'),
        (r'^i18n/', include('django.conf.urls.i18n')),
    )

Our home and admin pages do use i18n::

    urlpatterns += i18n_patterns("",
        # Home page for each language
        url(r"^$", views.home, name="home"),
        # Admin
        url(r'^admin/', include(admin.site.urls)),
    )

You may be able to use or prefer mezzanine.urls instead of including the url's in your urls.py

Views
-----

This demo application uses only a couple of views, one to redirect to the destination page after the language has been set and the home page.

When a user clicks a language button, it has two pieces of information, the language the visitor want to change to and the page they want to see.

The first part of the view tries to set the language id using settings.LANGUAGE_SITE_MAP, then the second part tries to find the right page for the user's language.::

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

The home page view brings together the multilingual home page with its metadata in thispage, summaries of the three pagetypes audience, you and marketing in fp_pages, and the list of alternate languages in hreflang_list.  Mezzanine is site aware so these queries just do the right thing.::

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

Templates
=========

As the whole site is multilingual two additions in templates/base.html add the language buttons and the alternative links.

As part of seo, search engines like to know if a page is available in an alternate language.

Google reference on alternate language support https://support.google.com/webmasters/answer/189077

If this is a multilingual page with a pagetype, then hreflang_list offers a list of alternate url's to be used in the document header.::

    {% for hreflang_href, hreflang_slug, hreflang_code in hreflang_list %}{% if hreflang_slug == '/' %}
        <link rel="alternate" hreflang="{{ hreflang_code }}" href="http://{{ hreflang_href }}{{ hreflang_slug }}" />
    {% else %}
        <link rel="alternate" hreflang="{{ hreflang_code }}" href="http://{{ hreflang_href }}/{{ hreflang_slug }}" />
    {% endif %}{% endfor %}

In the menu or where you would like your languages listed::

    <form id='frmLanguage' action="{% url 'set_language' %}" method="post">
    <div class='input-group input-group-sm' style='padding-top: 7px; width: 250px;'>
        {% csrf_token %}
        <input name="next" type="hidden" value="{% if page.mlpage.pagetype %}{% url 'redirect' page.mlpage.pagetype %}{% else %}/redirect/home{% endif %}" />
        {% for language, language_name in languages %}
        <button type="submit" name="language" value="{{ language }}"
        class="btn btn-sm btn-default" style="border-width:0;"
        title="{{ language_name }}" >
        <img src='{% static "img/" %}{{ language }}-125.png' alt="{{ language_name }}" style='width:25px;'>
        </button>
        {% endfor %}
    </div>
    </form>

This form has image buttons with their value as the language the visitor can change to and the 'next' hidden input with its value set to the page type.  When a visitor clicks their button of choice, the Django internationalization process occurs and the language is set accordingly, then forwards the request to the redirect_pagetype view that sets the site id according to the new language then forwards to the appropriate page.

Notes
=====

Export marketing is easier when the tools such as multilingual websites just work.  These are some of the contributing factors.
Components

Django is the base framework using the Python language.  This offers what we at Persistent Objects consider one of the best frameworks for building web applications.

Mezzanine is built on the Django framework for a powerful yet flexible and easy to use content management system.  Its sites management makes it easy to build multilingual sites, and when patched bring multilingual site capability into a single website.

Mezzanine BS Headers for managing great headline grabbing effective home page banners.
Visual design

Bootstrap is often our preferred choice for websites that are targeted at smart phones, tablets and desktops. Bootstrap offers a rich and well maintained interface that is easy to use.  Marketing is easier when high expectations are matched with a visually appealing interface.  Exporting to emerging markets with higher smart phone penetration than desktops is just as easy.
Scalable

A well designed Django application can scale well.  By separating the application from any static assets or media content offers significant security benefits as well as scalability.  Compared to development time, hardware is cheap, and so Django is designed to take advantage of as much hardware as you need.

Re-use
======

Want to use this as a base for your project but with a different name? The stream editor is your friend.::

    sed -i '' 's/mldemo/example/g' manage.py
    sed -i '' 's/mldemo/example/g' mldemo/*.py
    sed -i '' 's/mldemo/example/g' templates/base.html
    mv mldemo/templates/mldemo mldemo/templates/example
    mv mldemo example

Don't forget to change the usernames, passwords and secrets.

做 (verb) zuò do, as in 做买卖 zuò măimai do business.  Try a `Google Search <https://www.google.co.uk/search?q=%E5%81%9A%E4%B9%B0%E5%8D%96>`_. It is also the last character in the Pocket Oxford Chinese Dictonary.

by Alan Hicks

Check out `Alan's Google+ profile <https://plus.google.com/103014117568943351106>`_
