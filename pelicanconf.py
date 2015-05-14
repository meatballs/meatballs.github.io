#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Owen'
SITENAME = u'Owen Campbell'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en_GB'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ('plugins',)
PLUGINS = ['creole_reader', ]

THEME = 'themes/pelican-bootstrap3/'
BOOTSTRAP_THEME = 'cerulean'
DISPLAY_TAGS_ON_SIDEBAR = False
ABOUT_ME = 'Freelance consulting engineer.'
AVATAR = 'images/owencampbell.jpg'
SOCIAL = (
    ('Google+', 'http://plus.google.com/+OwenCampbell1'),
    ('Twitter', 'https://twitter.com/opcampbell'),
    ('LinkedIn', 'https://www.linkedin.com/in/owencampbell'),
    ('BitBucket', 'http://bitbucket.org/meatballs'),
    ('GitHub', 'http://github.com/meatballs'))
