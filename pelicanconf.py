#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'python-sapporo'
SITENAME = 'python-sapporo'
SITEURL = 'http://python-sapporo.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('connpass グループ', 'https://python-sapporo.connpass.com/'),
         ('Slack チャンネル', 'https://pysap.slack.com/messages/pysap/'),
         ('メーリングリスト', 'https://groups.google.co.jp/group/python-sapporo'),
         ('旧公式サイト', 'https://sites.google.com/site/pythonsapporo/'),
#         ('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.ico'},
}

THEME = "theme"
