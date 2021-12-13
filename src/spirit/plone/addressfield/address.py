# -*- coding: utf-8 -*-

from spirit.plone.addressfield.interfaces import IAddress
from zope.interface import implementer


@implementer(IAddress)
class Address(object):
    """Address object."""

    def __init__(self, address=None, postcode=None, place=None, region=None, country=None):
        self.address = address
        self.postcode = postcode
        self.place = place
        self.region = region
        self.country = country
