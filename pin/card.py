class Card(object):
    def __init__(
        self,
        number=None,
        expiry_month=None,
        expiry_year=None,
        cvc=None,
        name=None,
        address_line1=None,
        address_city=None,
        address_postcode=None,
        address_state=None,
        address_country=None,
        pin=None,
        *args,
        **kwargs
    ):
        self.number = number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.cvc = cvc
        self.name = name
        self.address_line1 = address_line1
        self.address_city = address_city
        self.address_postcode = address_postcode
        self.address_state = address_state
        self.address_country = address_country

    def build_payload(self):
        wanted_keys = [
            'number',
            'expiry_month',
            'expiry_year',
            'cvc',
            'name',
            'address_line1',
            'address_city',
            'address_postcode',
            'address_state',
            'address_country'
        ]
        payload = {}
        for k, v in self.__dict__.items():
            if k in wanted_keys:
                payload[k] = v

        return payload


    def save(self):
        if self.pin is not None:
            payload = self.build_payload()
            return self.pin.call_api('post', 'cards', payload)
        else:
            raise Exception('Pin instance not bound to this charge')