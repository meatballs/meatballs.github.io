#sta!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Owen Campbell'
SITENAME = u'Owen Campbell'
SITEURL = 'http://localhost:8000'

DEFAULT_METADATA = {
    'status': 'draft',
    'author': 'Owen Campbell'
}

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en_GB'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
# MENUITEMS = [('Projects', '/category/projects.html')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATHS = ('../pelican-plugins',)
PLUGINS = [
  'creole_reader',
  'series',
  ]

STATIC_PATHS = ['images', 'docs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

THEME = '../pelican-themes/pelican-bootstrap3/'
FAVICON = 'images/favicon/favicon.ico'
BOOTSTRAP_THEME = 'cerulean'
PYGMENTS_STYLE = 'solarizedlight'

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
    <li>District Commissioner for
    <a href="http://www.merseyweaverscouts.org.uk/">Mersey Weaver Scout District</a></li>
    <li>Founding Trustee of the UK Python Association</li>
  </ul>""")
AVATAR = '/images/favicon/favicon-310.png'
SHARIFF = True
SHARIFF_LANG = 'en'
DOCUTIL_CSS = True
USE_OPEN_GRAPH = True
TWITTER_CARDS = False
# TWITTER_USERNAME = 'opcampbell'
# TWITTER_WIDGET_ID = '598804695734431744'
SOCIAL = (
    ('Google+', 'http://plus.google.com/+OwenCampbell1'),
    ('Twitter', 'https://twitter.com/opcampbell'),
    ('LinkedIn', 'https://www.linkedin.com/in/owencampbell'),
    ('GitHub', 'http://github.com/meatballs'))
LINKS = (
  ('Metrophase', 'http://www.metrophase.co.uk'),
  ('Empiria', 'http://www.empiria.co.uk'),
  ('Mersey Weaver Scouts', 'http://www.merseyweaverscouts.org.uk'),
  )
