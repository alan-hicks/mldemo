# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mlpage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Pagetype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('glyphicon', models.CharField(max_length=35, verbose_name=b'Icon', choices=[(b'asterisk', b'glyphicon-asterisk'), (b'plus', b'glyphicon-plus'), (b'euro', b'glyphicon-euro'), (b'minus', b'glyphicon-minus'), (b'cloud', b'glyphicon-cloud'), (b'envelope', b'glyphicon-envelope'), (b'pencil', b'glyphicon-pencil'), (b'glass', b'glyphicon-glass'), (b'music', b'glyphicon-music'), (b'search', b'glyphicon-search'), (b'heart', b'glyphicon-heart'), (b'star', b'glyphicon-star'), (b'star-empty', b'glyphicon-star-empty'), (b'user', b'glyphicon-user'), (b'film', b'glyphicon-film'), (b'th-large', b'glyphicon-th-large'), (b'th', b'glyphicon-th'), (b'th-list', b'glyphicon-th-list'), (b'ok', b'glyphicon-ok'), (b'remove', b'glyphicon-remove'), (b'zoom-in', b'glyphicon-zoom-in'), (b'zoom-out', b'glyphicon-zoom-out'), (b'off', b'glyphicon-off'), (b'signal', b'glyphicon-signal'), (b'cog', b'glyphicon-cog'), (b'trash', b'glyphicon-trash'), (b'home', b'glyphicon-home'), (b'file', b'glyphicon-file'), (b'time', b'glyphicon-time'), (b'road', b'glyphicon-road'), (b'download-alt', b'glyphicon-download-alt'), (b'download', b'glyphicon-download'), (b'upload', b'glyphicon-upload'), (b'inbox', b'glyphicon-inbox'), (b'play-circle', b'glyphicon-play-circle'), (b'repeat', b'glyphicon-repeat'), (b'refresh', b'glyphicon-refresh'), (b'list-alt', b'glyphicon-list-alt'), (b'lock', b'glyphicon-lock'), (b'flag', b'glyphicon-flag'), (b'headphones', b'glyphicon-headphones'), (b'volume-off', b'glyphicon-volume-off'), (b'volume-down', b'glyphicon-volume-down'), (b'volume-up', b'glyphicon-volume-up'), (b'qrcode', b'glyphicon-qrcode'), (b'barcode', b'glyphicon-barcode'), (b'tag', b'glyphicon-tag'), (b'tags', b'glyphicon-tags'), (b'book', b'glyphicon-book'), (b'bookmark', b'glyphicon-bookmark'), (b'print', b'glyphicon-print'), (b'camera', b'glyphicon-camera'), (b'font', b'glyphicon-font'), (b'bold', b'glyphicon-bold'), (b'italic', b'glyphicon-italic'), (b'text-height', b'glyphicon-text-height'), (b'text-width', b'glyphicon-text-width'), (b'align-left', b'glyphicon-align-left'), (b'align-center', b'glyphicon-align-center'), (b'align-right', b'glyphicon-align-right'), (b'align-justify', b'glyphicon-align-justify'), (b'list', b'glyphicon-list'), (b'indent-left', b'glyphicon-indent-left'), (b'indent-right', b'glyphicon-indent-right'), (b'facetime-video', b'glyphicon-facetime-video'), (b'picture', b'glyphicon-picture'), (b'map-marker', b'glyphicon-map-marker'), (b'adjust', b'glyphicon-adjust'), (b'tint', b'glyphicon-tint'), (b'edit', b'glyphicon-edit'), (b'share', b'glyphicon-share'), (b'check', b'glyphicon-check'), (b'move', b'glyphicon-move'), (b'step-backward', b'glyphicon-step-backward'), (b'fast-backward', b'glyphicon-fast-backward'), (b'backward', b'glyphicon-backward'), (b'play', b'glyphicon-play'), (b'pause', b'glyphicon-pause'), (b'stop', b'glyphicon-stop'), (b'forward', b'glyphicon-forward'), (b'fast-forward', b'glyphicon-fast-forward'), (b'step-forward', b'glyphicon-step-forward'), (b'eject', b'glyphicon-eject'), (b'chevron-left', b'glyphicon-chevron-left'), (b'chevron-right', b'glyphicon-chevron-right'), (b'plus-sign', b'glyphicon-plus-sign'), (b'minus-sign', b'glyphicon-minus-sign'), (b'remove-sign', b'glyphicon-remove-sign'), (b'ok-sign', b'glyphicon-ok-sign'), (b'question-sign', b'glyphicon-question-sign'), (b'info-sign', b'glyphicon-info-sign'), (b'screenshot', b'glyphicon-screenshot'), (b'remove-circle', b'glyphicon-remove-circle'), (b'ok-circle', b'glyphicon-ok-circle'), (b'ban-circle', b'glyphicon-ban-circle'), (b'arrow-left', b'glyphicon-arrow-left'), (b'arrow-right', b'glyphicon-arrow-right'), (b'arrow-up', b'glyphicon-arrow-up'), (b'arrow-down', b'glyphicon-arrow-down'), (b'share-alt', b'glyphicon-share-alt'), (b'resize-full', b'glyphicon-resize-full'), (b'resize-small', b'glyphicon-resize-small'), (b'exclamation-sign', b'glyphicon-exclamation-sign'), (b'gift', b'glyphicon-gift'), (b'leaf', b'glyphicon-leaf'), (b'fire', b'glyphicon-fire'), (b'eye-open', b'glyphicon-eye-open'), (b'eye-close', b'glyphicon-eye-close'), (b'warning-sign', b'glyphicon-warning-sign'), (b'plane', b'glyphicon-plane'), (b'calendar', b'glyphicon-calendar'), (b'random', b'glyphicon-random'), (b'comment', b'glyphicon-comment'), (b'magnet', b'glyphicon-magnet'), (b'chevron-up', b'glyphicon-chevron-up'), (b'chevron-down', b'glyphicon-chevron-down'), (b'retweet', b'glyphicon-retweet'), (b'shopping-cart', b'glyphicon-shopping-cart'), (b'folder-close', b'glyphicon-folder-close'), (b'folder-open', b'glyphicon-folder-open'), (b'resize-vertical', b'glyphicon-resize-vertical'), (b'resize-horizontal', b'glyphicon-resize-horizontal'), (b'hdd', b'glyphicon-hdd'), (b'bullhorn', b'glyphicon-bullhorn'), (b'bell', b'glyphicon-bell'), (b'certificate', b'glyphicon-certificate'), (b'thumbs-up', b'glyphicon-thumbs-up'), (b'thumbs-down', b'glyphicon-thumbs-down'), (b'hand-right', b'glyphicon-hand-right'), (b'hand-left', b'glyphicon-hand-left'), (b'hand-up', b'glyphicon-hand-up'), (b'hand-down', b'glyphicon-hand-down'), (b'circle-arrow-right', b'glyphicon-circle-arrow-right'), (b'circle-arrow-left', b'glyphicon-circle-arrow-left'), (b'circle-arrow-up', b'glyphicon-circle-arrow-up'), (b'circle-arrow-down', b'glyphicon-circle-arrow-down'), (b'globe', b'glyphicon-globe'), (b'wrench', b'glyphicon-wrench'), (b'tasks', b'glyphicon-tasks'), (b'filter', b'glyphicon-filter'), (b'briefcase', b'glyphicon-briefcase'), (b'fullscreen', b'glyphicon-fullscreen'), (b'dashboard', b'glyphicon-dashboard'), (b'paperclip', b'glyphicon-paperclip'), (b'heart-empty', b'glyphicon-heart-empty'), (b'link', b'glyphicon-link'), (b'phone', b'glyphicon-phone'), (b'pushpin', b'glyphicon-pushpin'), (b'usd', b'glyphicon-usd'), (b'gbp', b'glyphicon-gbp'), (b'sort', b'glyphicon-sort'), (b'sort-by-alphabet', b'glyphicon-sort-by-alphabet'), (b'sort-by-alphabet-alt', b'glyphicon-sort-by-alphabet-alt'), (b'sort-by-order', b'glyphicon-sort-by-order'), (b'sort-by-order-alt', b'glyphicon-sort-by-order-alt'), (b'sort-by-attributes', b'glyphicon-sort-by-attributes'), (b'sort-by-attributes-alt', b'glyphicon-sort-by-attributes-alt'), (b'unchecked', b'glyphicon-unchecked'), (b'expand', b'glyphicon-expand'), (b'collapse-down', b'glyphicon-collapse-down'), (b'collapse-up', b'glyphicon-collapse-up'), (b'log-in', b'glyphicon-log-in'), (b'flash', b'glyphicon-flash'), (b'log-out', b'glyphicon-log-out'), (b'new-window', b'glyphicon-new-window'), (b'record', b'glyphicon-record'), (b'save', b'glyphicon-save'), (b'open', b'glyphicon-open'), (b'saved', b'glyphicon-saved'), (b'import', b'glyphicon-import'), (b'export', b'glyphicon-export'), (b'send', b'glyphicon-send'), (b'floppy-disk', b'glyphicon-floppy-disk'), (b'floppy-saved', b'glyphicon-floppy-saved'), (b'floppy-remove', b'glyphicon-floppy-remove'), (b'floppy-save', b'glyphicon-floppy-save'), (b'floppy-open', b'glyphicon-floppy-open'), (b'credit-card', b'glyphicon-credit-card'), (b'transfer', b'glyphicon-transfer'), (b'cutlery', b'glyphicon-cutlery'), (b'header', b'glyphicon-header'), (b'compressed', b'glyphicon-compressed'), (b'earphone', b'glyphicon-earphone'), (b'phone-alt', b'glyphicon-phone-alt'), (b'tower', b'glyphicon-tower'), (b'stats', b'glyphicon-stats'), (b'sd-video', b'glyphicon-sd-video'), (b'hd-video', b'glyphicon-hd-video'), (b'subtitles', b'glyphicon-subtitles'), (b'sound-stereo', b'glyphicon-sound-stereo'), (b'sound-dolby', b'glyphicon-sound-dolby'), (b'sound-5-1', b'glyphicon-sound-5-1'), (b'sound-6-1', b'glyphicon-sound-6-1'), (b'sound-7-1', b'glyphicon-sound-7-1'), (b'copyright-mark', b'glyphicon-copyright-mark'), (b'registration-mark', b'glyphicon-registration-mark'), (b'cloud-download', b'glyphicon-cloud-download'), (b'cloud-upload', b'glyphicon-cloud-upload'), (b'tree-conifer', b'glyphicon-tree-conifer'), (b'tree-deciduous', b'glyphicon-tree-deciduous')])),
                ('description', models.CharField(max_length=50, verbose_name=b'Description')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Page type',
                'verbose_name_plural': 'Page types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mlpage',
            name='pagetype',
            field=models.ForeignKey(blank=True, to='mldemo.Pagetype', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Typestatus',
            fields=[
            ],
            options={
                'ordering': ['domain', 'title'],
                'verbose_name': 'Translation status',
                'managed': False,
                'verbose_name_plural': 'Translation status',
            },
            bases=(models.Model,),
        ),
    ]
