#----------------------------------------------------------------------
# Copyright (c) 2014-2016, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
Multilingual demo models
"""

from django.db import models

from mezzanine.core.models import RichText
from mezzanine.pages.models import Page

class Pagetype(models.Model):
    """
    Page type used for joining pages and sites
    """
    GLYPHICON_CHOICES = (
        ('asterisk', 'glyphicon-asterisk'),
        ('plus', 'glyphicon-plus'),
        ('euro', 'glyphicon-euro'),
        ('minus', 'glyphicon-minus'),
        ('cloud', 'glyphicon-cloud'),
        ('envelope', 'glyphicon-envelope'),
        ('pencil', 'glyphicon-pencil'),
        ('glass', 'glyphicon-glass'),
        ('music', 'glyphicon-music'),
        ('search', 'glyphicon-search'),
        ('heart', 'glyphicon-heart'),
        ('star', 'glyphicon-star'),
        ('star-empty', 'glyphicon-star-empty'),
        ('user', 'glyphicon-user'),
        ('film', 'glyphicon-film'),
        ('th-large', 'glyphicon-th-large'),
        ('th', 'glyphicon-th'),
        ('th-list', 'glyphicon-th-list'),
        ('ok', 'glyphicon-ok'),
        ('remove', 'glyphicon-remove'),
        ('zoom-in', 'glyphicon-zoom-in'),
        ('zoom-out', 'glyphicon-zoom-out'),
        ('off', 'glyphicon-off'),
        ('signal', 'glyphicon-signal'),
        ('cog', 'glyphicon-cog'),
        ('trash', 'glyphicon-trash'),
        ('home', 'glyphicon-home'),
        ('file', 'glyphicon-file'),
        ('time', 'glyphicon-time'),
        ('road', 'glyphicon-road'),
        ('download-alt', 'glyphicon-download-alt'),
        ('download', 'glyphicon-download'),
        ('upload', 'glyphicon-upload'),
        ('inbox', 'glyphicon-inbox'),
        ('play-circle', 'glyphicon-play-circle'),
        ('repeat', 'glyphicon-repeat'),
        ('refresh', 'glyphicon-refresh'),
        ('list-alt', 'glyphicon-list-alt'),
        ('lock', 'glyphicon-lock'),
        ('flag', 'glyphicon-flag'),
        ('headphones', 'glyphicon-headphones'),
        ('volume-off', 'glyphicon-volume-off'),
        ('volume-down', 'glyphicon-volume-down'),
        ('volume-up', 'glyphicon-volume-up'),
        ('qrcode', 'glyphicon-qrcode'),
        ('barcode', 'glyphicon-barcode'),
        ('tag', 'glyphicon-tag'),
        ('tags', 'glyphicon-tags'),
        ('book', 'glyphicon-book'),
        ('bookmark', 'glyphicon-bookmark'),
        ('print', 'glyphicon-print'),
        ('camera', 'glyphicon-camera'),
        ('font', 'glyphicon-font'),
        ('bold', 'glyphicon-bold'),
        ('italic', 'glyphicon-italic'),
        ('text-height', 'glyphicon-text-height'),
        ('text-width', 'glyphicon-text-width'),
        ('align-left', 'glyphicon-align-left'),
        ('align-center', 'glyphicon-align-center'),
        ('align-right', 'glyphicon-align-right'),
        ('align-justify', 'glyphicon-align-justify'),
        ('list', 'glyphicon-list'),
        ('indent-left', 'glyphicon-indent-left'),
        ('indent-right', 'glyphicon-indent-right'),
        ('facetime-video', 'glyphicon-facetime-video'),
        ('picture', 'glyphicon-picture'),
        ('map-marker', 'glyphicon-map-marker'),
        ('adjust', 'glyphicon-adjust'),
        ('tint', 'glyphicon-tint'),
        ('edit', 'glyphicon-edit'),
        ('share', 'glyphicon-share'),
        ('check', 'glyphicon-check'),
        ('move', 'glyphicon-move'),
        ('step-backward', 'glyphicon-step-backward'),
        ('fast-backward', 'glyphicon-fast-backward'),
        ('backward', 'glyphicon-backward'),
        ('play', 'glyphicon-play'),
        ('pause', 'glyphicon-pause'),
        ('stop', 'glyphicon-stop'),
        ('forward', 'glyphicon-forward'),
        ('fast-forward', 'glyphicon-fast-forward'),
        ('step-forward', 'glyphicon-step-forward'),
        ('eject', 'glyphicon-eject'),
        ('chevron-left', 'glyphicon-chevron-left'),
        ('chevron-right', 'glyphicon-chevron-right'),
        ('plus-sign', 'glyphicon-plus-sign'),
        ('minus-sign', 'glyphicon-minus-sign'),
        ('remove-sign', 'glyphicon-remove-sign'),
        ('ok-sign', 'glyphicon-ok-sign'),
        ('question-sign', 'glyphicon-question-sign'),
        ('info-sign', 'glyphicon-info-sign'),
        ('screenshot', 'glyphicon-screenshot'),
        ('remove-circle', 'glyphicon-remove-circle'),
        ('ok-circle', 'glyphicon-ok-circle'),
        ('ban-circle', 'glyphicon-ban-circle'),
        ('arrow-left', 'glyphicon-arrow-left'),
        ('arrow-right', 'glyphicon-arrow-right'),
        ('arrow-up', 'glyphicon-arrow-up'),
        ('arrow-down', 'glyphicon-arrow-down'),
        ('share-alt', 'glyphicon-share-alt'),
        ('resize-full', 'glyphicon-resize-full'),
        ('resize-small', 'glyphicon-resize-small'),
        ('exclamation-sign', 'glyphicon-exclamation-sign'),
        ('gift', 'glyphicon-gift'),
        ('leaf', 'glyphicon-leaf'),
        ('fire', 'glyphicon-fire'),
        ('eye-open', 'glyphicon-eye-open'),
        ('eye-close', 'glyphicon-eye-close'),
        ('warning-sign', 'glyphicon-warning-sign'),
        ('plane', 'glyphicon-plane'),
        ('calendar', 'glyphicon-calendar'),
        ('random', 'glyphicon-random'),
        ('comment', 'glyphicon-comment'),
        ('magnet', 'glyphicon-magnet'),
        ('chevron-up', 'glyphicon-chevron-up'),
        ('chevron-down', 'glyphicon-chevron-down'),
        ('retweet', 'glyphicon-retweet'),
        ('shopping-cart', 'glyphicon-shopping-cart'),
        ('folder-close', 'glyphicon-folder-close'),
        ('folder-open', 'glyphicon-folder-open'),
        ('resize-vertical', 'glyphicon-resize-vertical'),
        ('resize-horizontal', 'glyphicon-resize-horizontal'),
        ('hdd', 'glyphicon-hdd'),
        ('bullhorn', 'glyphicon-bullhorn'),
        ('bell', 'glyphicon-bell'),
        ('certificate', 'glyphicon-certificate'),
        ('thumbs-up', 'glyphicon-thumbs-up'),
        ('thumbs-down', 'glyphicon-thumbs-down'),
        ('hand-right', 'glyphicon-hand-right'),
        ('hand-left', 'glyphicon-hand-left'),
        ('hand-up', 'glyphicon-hand-up'),
        ('hand-down', 'glyphicon-hand-down'),
        ('circle-arrow-right', 'glyphicon-circle-arrow-right'),
        ('circle-arrow-left', 'glyphicon-circle-arrow-left'),
        ('circle-arrow-up', 'glyphicon-circle-arrow-up'),
        ('circle-arrow-down', 'glyphicon-circle-arrow-down'),
        ('globe', 'glyphicon-globe'),
        ('wrench', 'glyphicon-wrench'),
        ('tasks', 'glyphicon-tasks'),
        ('filter', 'glyphicon-filter'),
        ('briefcase', 'glyphicon-briefcase'),
        ('fullscreen', 'glyphicon-fullscreen'),
        ('dashboard', 'glyphicon-dashboard'),
        ('paperclip', 'glyphicon-paperclip'),
        ('heart-empty', 'glyphicon-heart-empty'),
        ('link', 'glyphicon-link'),
        ('phone', 'glyphicon-phone'),
        ('pushpin', 'glyphicon-pushpin'),
        ('usd', 'glyphicon-usd'),
        ('gbp', 'glyphicon-gbp'),
        ('sort', 'glyphicon-sort'),
        ('sort-by-alphabet', 'glyphicon-sort-by-alphabet'),
        ('sort-by-alphabet-alt', 'glyphicon-sort-by-alphabet-alt'),
        ('sort-by-order', 'glyphicon-sort-by-order'),
        ('sort-by-order-alt', 'glyphicon-sort-by-order-alt'),
        ('sort-by-attributes', 'glyphicon-sort-by-attributes'),
        ('sort-by-attributes-alt', 'glyphicon-sort-by-attributes-alt'),
        ('unchecked', 'glyphicon-unchecked'),
        ('expand', 'glyphicon-expand'),
        ('collapse-down', 'glyphicon-collapse-down'),
        ('collapse-up', 'glyphicon-collapse-up'),
        ('log-in', 'glyphicon-log-in'),
        ('flash', 'glyphicon-flash'),
        ('log-out', 'glyphicon-log-out'),
        ('new-window', 'glyphicon-new-window'),
        ('record', 'glyphicon-record'),
        ('save', 'glyphicon-save'),
        ('open', 'glyphicon-open'),
        ('saved', 'glyphicon-saved'),
        ('import', 'glyphicon-import'),
        ('export', 'glyphicon-export'),
        ('send', 'glyphicon-send'),
        ('floppy-disk', 'glyphicon-floppy-disk'),
        ('floppy-saved', 'glyphicon-floppy-saved'),
        ('floppy-remove', 'glyphicon-floppy-remove'),
        ('floppy-save', 'glyphicon-floppy-save'),
        ('floppy-open', 'glyphicon-floppy-open'),
        ('credit-card', 'glyphicon-credit-card'),
        ('transfer', 'glyphicon-transfer'),
        ('cutlery', 'glyphicon-cutlery'),
        ('header', 'glyphicon-header'),
        ('compressed', 'glyphicon-compressed'),
        ('earphone', 'glyphicon-earphone'),
        ('phone-alt', 'glyphicon-phone-alt'),
        ('tower', 'glyphicon-tower'),
        ('stats', 'glyphicon-stats'),
        ('sd-video', 'glyphicon-sd-video'),
        ('hd-video', 'glyphicon-hd-video'),
        ('subtitles', 'glyphicon-subtitles'),
        ('sound-stereo', 'glyphicon-sound-stereo'),
        ('sound-dolby', 'glyphicon-sound-dolby'),
        ('sound-5-1', 'glyphicon-sound-5-1'),
        ('sound-6-1', 'glyphicon-sound-6-1'),
        ('sound-7-1', 'glyphicon-sound-7-1'),
        ('copyright-mark', 'glyphicon-copyright-mark'),
        ('registration-mark', 'glyphicon-registration-mark'),
        ('cloud-download', 'glyphicon-cloud-download'),
        ('cloud-upload', 'glyphicon-cloud-upload'),
        ('tree-conifer', 'glyphicon-tree-conifer'),
        ('tree-deciduous', 'glyphicon-tree-deciduous'),
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
        #pylint: disable=too-few-public-methods
        verbose_name = "Page type"
        verbose_name_plural = "Page types"
        ordering = ['title']

class Mlpage(Page, RichText):
    """
    Subclass of Mezzanine page adding page type
    """
    #pylint: disable=too-many-ancestors,too-many-public-methods
    pagetype = models.ForeignKey(Pagetype, blank=True, null=True)

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
        #pylint: disable=too-few-public-methods
        verbose_name = "Translation status"
        verbose_name_plural = "Translation status"
        managed = False
        ordering = ['domain', 'title']
#SQL for language coverage
#SELECT j.site_id, j.domain, j.type_id, j.title, count(p.id) pages
#FROM (
#    SELECT p.id, p.site_id, mp.pagetype_id
#    FROM pages_page p
#    INNER JOIN mldemo_mlpage mp ON p.id = mp.page_ptr_id
#    ) AS p
#RIGHT OUTER JOIN (
#    SELECT s.id as site_id, s.domain, t.id as type_id, t.title
#    FROM django_site s
#    INNER JOIN mldemo_pagetype t ON TRUE) AS j
#ON p.site_id = j.site_id
#AND p.pagetype_id = j.type_id
#GROUP BY j.site_id, j.domain, j.type_id, j.title;
