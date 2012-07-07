import requests

class Pin(object):
    def __init__(self, mode, api_key, *args, **kwargs):

        # sets connection mode
        if mode == 'test':
            self._mode = 'test'
        elif mode == 'live':
            self._mode = 'live'
        else: raise Exception('Invalid mode. Must be test or live')

        if type(api_key) is type(str()):
            self._api_key = api_key
        else: raise Exception('api_key must be a string')

    @property
    def api_url(self):
        if self._mode == 'test':
            return 'https://test-api.pin.net.au/1/'
        else:
            return 'https://api.pin.net.au/1/'

    @property
    def charges(self):
        url = "%scharges" % self.api_url
        request = requests.get(url, auth=(self._api_key+':', ''))
        return request.json