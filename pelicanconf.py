#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Owen Campbell'
SITENAME = u'Owen Campbell'
SITEURL = 'http://localhost:8000'

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en_GB'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATHS = ('plugins',)
PLUGINS = [
  'creole_reader',
  'series',
  ]

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = 'themes/pelican-bootstrap3/'
FAVICON = 'images/favicon/favicon.ico'
BOOTSTRAP_THEME = 'cerulean'
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_SERIES_ON_SIDEBAR = False
SHOW_SERIES = True
ABOUT_ME = ("""
  <ul>
    <li>Chartered Engineer</li>
    <li>Based near Chester, UK.</li>
    <li>Specialises in technical leadership of software development and
    implementation projects.</li>
    <li>Particularly enjoys taking on projects in need of rescue!</li>
    <li>Volunteers as District Commissioner for
    <a href='http://www.merseyweaverscouts.org.uk' target='_blank'>
    Mersey Weaver Scout District</a></li>
  </ul>""")
AVATAR = '/images/favicon/favicon-310.png'
SHARIFF = True
SHARIFF_LANG = 'en'
DOCUTIL_CSS = True
USE_OPEN_GRAPH = True
TWITTER_CARDS = True
TWITTER_USERNAME = 'opcampbell'
TWITTER_WIDGET_ID = '598804695734431744'
SOCIAL = (
    ('Google+', 'http://plus.google.com/+OwenCampbell1'),
    ('Twitter', 'https://twitter.com/opcampbell'),
    ('LinkedIn', 'https://www.linkedin.com/in/owencampbell'),
    ('GitHub', 'http://github.com/meatballs'))
