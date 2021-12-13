# -*- coding: utf-8 -*-

from spirit.plone.addressfield.address import Address
from spirit.plone.addressfield.interfaces import IAddress
from spirit.plone.addressfield.interfaces import IAddressField
from zope import schema
from zope.interface import implementer


@implementer(IAddressField)
class AddressField(schema.Object):
    """A custom field for addresses."""

    _type = Address
    schema = IAddress

    def __init__(self, **kw):
        super(AddressField, self).__init__(schema=self.schema, **kw)
