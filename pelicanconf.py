# sta!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Owen Campbell"
SITENAME = "Owen Campbell"
SITEURL = "http://localhost:8000"

DEFAULT_METADATA = {"status": "draft", "author": "Owen Campbell"}

PATH = "content"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en_GB"
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
# MENUITEMS = [('Projects', '/category/projects.html')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATHS = ("../pelican-plugins",)
PLUGINS = ["creole_reader", "series", "pelican-ipynb.markup", "tag_cloud"]

MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]

STATIC_PATHS = ["images", "docs", "extra/CNAME", "extra/keybase.txt"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/keybase.txt": {"path": "keybase.txt"},
}

THEME = "../pelican-themes/pelican-bootstrap3/"
FAVICON = "images/favicon/favicon.ico"
BOOTSTRAP_THEME = "cerulean"
PYGMENTS_STYLE = "solarizedlight"

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_SERIES_ON_SIDEBAR = False
SHOW_SERIES = True
ABOUT_ME = """
  <ul>
    <li>Freelancer, available for hire</li>
    <li>Chartered Engineer</li>
    <li>Based near Chester, UK.</li>
    <li>Specialises in technical leadership of software development and
    implementation projects.</li>
    <li>Particularly enjoys taking on projects in need of rescue!</li>
    <li>Python Enthusiast</li>
    <li>Founding Trustee of the UK Python Association</li>
  </ul>"""
AVATAR = "/images/favicon/favicon-310.png"
SHARIFF = True
SHARIFF_LANG = "en"
DOCUTIL_CSS = True
USE_OPEN_GRAPH = True
TWITTER_CARDS = False
# TWITTER_USERNAME = 'opcampbell'
# TWITTER_WIDGET_ID = '598804695734431744'
SOCIAL = (
    ("Twitter", "https://twitter.com/opcampbell"),
    ("LinkedIn", "https://www.linkedin.com/in/owencampbell"),
    ("GitHub", "https://github.com/meatballs"),
)
LINKS = (
    ("SQL Python Tutorial", "https://owencampbell.me.uk/sql_python_tutorial"),
    ("Empiria", "https://www.empiria.co.uk"),
)
