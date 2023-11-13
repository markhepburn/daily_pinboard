#!/usr/bin/env python
import datetime
import os
import random
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        # If using posts/recent for testing, return bookmarks['posts']
        return bookmarks

    def random_bookmarks(self, num_bookmarks):
        bookmarks = self.get_bookmarks()
        return random.sample(bookmarks, num_bookmarks)


class EmailEndpoint:
    def __init__(self, envdict=None):
        super().__init__()
        if not envdict:
            envdict = os.environ
        self._load(envdict)

    def _load(self, envdict):
        # Throw a KeyError if configuration isn't set:
        self.server = envdict['SMTP_SERVER']
        self.username = envdict['SMTP_USERNAME']
        self.password = envdict['SMTP_PASSWORD']
        self.email = envdict['EMAIL']

    def create_msg(self, msg_html):
        msg = MIMEMultipart()
        msg['Subject'] = "Your Pinboard Daily 5"
        msg['From'] = self.email
        msg['To'] = self.email
        msg.attach(MIMEText(msg_html, 'html'))

        return msg

    def send_msg(self, msg):
        with smtplib.SMTP_SSL(host=self.server, port=465) as server:
            server.login(self.username, self.password)
            server.send_message(msg)


def enrich_data(bookmarks):
    """Data conversion, any enrichment necessary"""
    # The mutating side-effects make my skin crawl now, but I'll live with it here:
    for bookmark in bookmarks:
        # parse date
        date_formatted = datetime.date.fromisoformat(bookmark['time'][:10])
        bookmark['date_formatted'] = date_formatted.strftime('%d %b, %Y')
        # split tags
        bookmark['tags'] = bookmark['tags'].split(None)
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

    email_endpoint = EmailEndpoint()
    msg = email_endpoint.create_msg(txt)
    email_endpoint.send_msg(msg)


if __name__ == '__main__':
    main()
