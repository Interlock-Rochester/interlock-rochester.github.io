#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Interlock Member'
SITENAME = u'Interlock Rochester - Rochester\'s Hackerspace'
SITEURL = 'https://interlockroc.org'

#FRONT_PIC_BACKGROUND = 'cut_wood_crop.jpg'
#FRONT_PIC_BACKGROUND = 'gear_on_table.jpg'
FRONT_PIC_BACKGROUND = 'invader_print_crop.jpg'
#FRONT_PIC_BACKGROUND = 'invader_w_blur_crop.jpg'
#FRONT_PIC_BACKGROUND = 'gear_on_wall.jpg'
#FRONT_PIC_BACKGROUND = 'plot_shape.jpg'
#FRONT_PIC_BACKGROUND = 'plot_words.jpg'
#FRONT_PIC_BACKGROUND = 'on_air.jpg'
#FRONT_PIC_BACKGROUND = 'on_air_crop.jpg'
#FRONT_PIC_BACKGROUND = 'electronics_bench_crop.jpg'

SITE_DESC = 'Interlock is a non-profit organization that provides space for its members and the local community to develop and share their interests in science, technology, art, and culture.'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = "./themes/clean-blog"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Wiki', 'http://wiki.interlockroc.org'),)

GITHUB_URL = 'https://github.com/Interlock-Rochester'
TWITTER_URL = 'https://twitter.com/interlockroc'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'wp-uploads']

#if we choose a them that shows this, we might want to put, eg, about.md in content/pages/
#DISPLAY_PAGES_ON_MENU = True

