# sta!/usr/bin/env pytho,
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Owen Campbell"
SITENAME = "Owen Campbell"
SITEURL = "http://localhost:8000"

DEFAULT_METADATA = {"status": "draft", "author": "Owen Campbell"}

PATH = "content"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"
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
PLUGINS = ["creole_reader", "series", "pelican-ipynb.markup", "tag_cloud", "i18n_subsites"]

MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_SKIP_CSS = True

CUSTOM_CSS = "static/css/custom.css"
STATIC_PATHS = [
    "images",
    "docs",
    "extra/CNAME",
    "extra/keybase.txt",
    "extra/custom.css",
]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/keybase.txt": {"path": "keybase.txt"},
    "extra/custom.css": {"path": "static/css/custom.css"},
}

# Tell Pelican to add files from 'extra' to the output dir
STATIC_PATHS = ["images", "extra"]

# Tell Pelican to change the path to 'static/custom.css' in the output dir


THEME = "../pelican-themes/pelican-bootstrap3/"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
FAVICON = "images/favicon/favicon-16x16.png"
BOOTSTRAP_THEME = "cerulean"
PYGMENTS_STYLE = "solarizedlight"

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_SERIES_ON_SIDEBAR = False
SHOW_SERIES = True
ABOUT_ME = """
  <ul>
    <li>Freelance Professional Software Engineer</li>
    <li>Chartered Engineer</li>
    <li>Based near Chester, UK.</li>
    <li>Python Enthusiast</li>
    <li>PyCon UK Organiser</li>
    <li>Founding Trustee of the UK Python Association</li>
  </ul>"""
AVATAR = "/images/favicon/mstile-310x310.png"
DOCUTIL_CSS = True
USE_OPEN_GRAPH = True
TWITTER_CARDS = False
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/owencampbell"),
    ("GitHub", "https://github.com/meatballs"),
)
LINKS = (
    ("SQL Python Tutorial", "https://www.owencampbell.me.uk/sql_python_tutorial"),
    ("PyCon UK", "https://pyconuk.org"),
    ("UK Python Association", "https://uk.python.org"),
)
