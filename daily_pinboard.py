#!/usr/bin/env python
import datetime
import os
import random

from mako.template import Template
import requests



# https://pinboard.in/api/v2/overview
# Might have to use v1; v2 doesn't seem to be available
class PinboardAPI:
    def __init__(self, envdict=None):
        super().__init__()
        if not envdict:
            envdict = os.environ
        self._load(envdict)

    def _load(self, envdict):
        # Throw a KeyError if configuration isn't set:
        self.endpoint = envdict['API_ENDPOINT']  # Allow swapping out of the test endpoints
        self.account_token = envdict['PINBOARD_TOKEN']
        self.email = envdict['EMAIL']

    def _api_get(self, url, **params):
        params = params or {}
        params.update({
            'auth_token': self.account_token,
            'format': 'json',
        })
        res = requests.get(self.endpoint + url, params=params)
        return res.json()

    def get_bookmarks(self):
        bookmarks = self._api_get('posts/all')
        return bookmarks['posts']

    def random_bookmarks(self, num_bookmarks):
        bookmarks = self.get_bookmarks()
        return random.sample(bookmarks, num_bookmarks)


def enrich_data(bookmarks):
    """Data conversion, any enrichment necessary"""
    # The mutating side-effects make my skin crawl now, but I'll live with it here:
    for bookmark in bookmarks:
        # parse date
        date_formatted = datetime.date.fromisoformat(bookmark['time'][:10])
        bookmark['date_formatted'] = date_formatted.strftime('%d %b, %Y')
        # split tags
        bookmark['tags'] = bookmark['tags'].split(' ')
    return bookmarks


def format_email(bookmarks):
    tmpl = Template(filename="email.tpl")
    txt = tmpl.render(bookmarks=bookmarks)
    return txt


def main():
    pinboard = PinboardAPI()
    daily_bookmarks = pinboard.random_bookmarks(5)
    daily_bookmarks = enrich_data(daily_bookmarks)
    txt = format_email(daily_bookmarks)
    with open('email.html', 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    main()
