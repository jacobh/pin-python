# Pin for Python
> A simple wrapper around pin.net.au's API

## Status
Currently in very early developemnt, basically it's not ready for use at all. I'm currently getting a few little proof-of-concepts working which I then want to transfer into the final product.

## Requirements
- [the latest version of kreitz/requests](https://github.com/kennethreitz/requests)

## Usage

### Listing Charges

```python
>>> import pin
>>> mypin = Pin('test', 'insert api key here')
>>> mypin.charges
[
  $10.000000 - enthral sub fee,
  $19.750000 - another test charge
]
>>> mypin.charges[0].__dict__
{
  'description': u'enthral sub fee',
  'amount': 1000,
  'ip_address': None,
  'email': u'jacob@haslehurst.net',
  'card': <pin.card.Card object at 0x10b40b810>,
  'pin': <pin.Pin object at 0x10b3f0c50>
}
```

### Creating A Charge

```python
>>> import pin
>>> mypin = pin.Pin('test', 'insert api key here')
>>> mycard = mypin.create_card(
    '5520000000000000',
    05,
    2013,
    123,
    'roland robot',
    '123 fake st',
    'Perth',
    6000,
    'WA',
    'AU'
)
>>> mycharge = mypin.create_charge(
    2000,
    'my description',
    'jacob@haslehurst.net',
    '127.0.0.1',
    mycard
)
>>> mycharge.save()
<Response [200]>
```