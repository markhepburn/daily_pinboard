#!/usr/bin/env python
import random

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

    def _api_get(self, endpoint, **params):
        # Auth: auth_token query param (or basic auth)
        pass

    def get_bookmarks(self):
        pass

    def random_bookmarks(self, num_bookmarks):
        pass

    # random.sample(lst, num) returns non-repeating elements


def enrich_data(bookmarks):
    """Placeholder for now; thinking is to add styling, without
    calculating that in the template"""
    return bookmarks


def format_email(bookmarks):
    tmpl = Template(filename="email.tpl")
    txt = tmpl.render(bookmarks=bookmarks)
    return txt

def main():
    pinboard = PinboardAPI()
    daily_bookmarks = pinboard.random_bookmarks(5)
    pass


if __name__ == '__main__':
    main()
