class Charge(object):
    def __init__(
        self,
        amount,
        description,
        email,
        ip_address,
        card=None,
        pin=None,
        *args,
        **kwargs
    ):
        self.amount = amount
        self.description = description
        self.email = email
        self.ip_address = ip_address
        self.card = card
        self.pin = pin

    def build_payload(self):
        d = {
            'amount': self.amount,
            'description': self.description,
            'email': self.email,
            'ip_address': self.ip_address,
        }

        for k, v in self.card.build_payload().items():
            d['card[%s]' % k] = v

        return d


    def save(self):
        if self.pin is not None:
            payload = self.build_payload()
            return self.pin.call_api('post', 'charges', payload)
        else:
            raise Exception('Pin instance not bound to this charge')

    def __repr__(self):
        return "$%f - %s" % (round(self.amount/100.0, 2), self.description)