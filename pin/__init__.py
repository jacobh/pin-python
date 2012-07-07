import requests
from .charge import Charge
from .card import Card
from .customer import Customer

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

    def call_api(self, method, action, payload=None):
        url = self.api_url + action

        if method == 'get':
            response = requests.get(url, auth=(self._api_key+':', ''))

        return response.json

    @property
    def charges(self):
        json = self.call_api('get', 'charges')

        charges = []
        for charge_dict in json['response']:
            charges.append(Charge(
                charge_dict['amount'],
                charge_dict['description'],
                charge_dict['email'],
                charge_dict['ip_address'],
                Card(),
                self
            ))
        return charges

    # these two currently aren't working, not sure why
    @property
    def cards(self):
        json = self.call_api('get', 'cards')
        return json

    @property
    def customers(self):
        json = self.call_api('get', 'customers')
        return json

    def create_charge(self, *args, **kwargs):
        charge = Charge(*args, **kwargs)