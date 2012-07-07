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

    def save(self):
        payload = {
            'amount': self.amount,
            'description': self.description,
            'email': self.email,
            'ip_address': self.ip_address,
            'card': self.card.__dict__
        }

        self.pin.call_api('charge', 'post', payload)

    def __repr__(self):
        return "$%f - %s" % (round(self.amount/100.0, 2), self.description)