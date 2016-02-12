# -*- coding: utf-8 -*-
from datetime import date

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils import feedgenerator

from .utils import get_all_categories, get_all_positions


class LatestPositionsFeed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed
    title = 'Current Mozilla job openings'
    description = ('The current list of job openings, available internships '
                   'and contract opportunities at Mozilla.')
    feed_copyright = ('Portions of this content are ©1998–%s by individual '
                      'mozilla.org contributors. Content available under a '
                      'Creative Commons license.' % date.today().year)

    def link(self):
        return reverse('careers.listings')

    def feed_url(self):
        return reverse('careers.feed')

    def categories(self):
        return get_all_categories()

    def items(self):
        return get_all_positions()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_categories(self, item):
        categories = []
        if item.category:
            categories.append(item.category.name)
        if item.location_filter:
            if item.location_filter == 'All':
                location = 'Worldwide'
            else:
                location = item.location_filter
            categories.append(location)
        return categories
