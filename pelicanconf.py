#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ptanguy'
SITENAME = u"ptanguy's blog"
SITEURL = ''

USE_FOLDER_AS_CATEGORY = False

PATH = 'content'
STATIC_PATHS = ['images','CNAME']
ARTICLE_PATHS = ['blog']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_METADATA = {
        'status': 'draft',
        }

# Feed generation is usually not desired when developing
#FEED_DOMAIN = None
#FEED_ATOM = None
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#FEED_RSS = 'feeds/rss.xml'
#CATEGORY_FEED_RSS = 'feeds/category/%s.rss.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#TRANSLATION_FEED_ATOM = None
#
## Feeds
#FEEDS = (('All posts', 'feeds/all.rss.xml'),
#                 ('Category', 'feeds/category'),)



#Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/phtanguy'),
        ('Github', 'https://github.com/ptanguy'),)

DEFAULT_PAGINATION = 10

#THEME = "pelican-themes/"
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'cosmo'

#Template settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

#Sidebar options
HIDE_SIDEBAR = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
