#!/usr/bin/env python


# https://pinboard.in/api/v2/overview
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

