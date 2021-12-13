# -*- coding: utf-8 -*-

from spirit.plone.addressfield.address import Address
from spirit.plone.addressfield.interfaces import IAddress
from spirit.plone.addressfield.interfaces import IAddressField
from spirit.plone.addressfield.interfaces import IAddressWidget
from z3c.form.converter import BaseDataConverter
from zope.component import adapter


@adapter(IAddressField, IAddressWidget)
class AddressConverter(BaseDataConverter):
    """Converts from an n-tuple to an Address."""

    def toWidgetValue(self, value):
        if value:
            return (value.address, value.postcode, value.place, value.region, value.country)

    def toFieldValue(self, value):
        if value is None:
            return self.field.missing_value

        if IAddress.providedBy(value):
            return value

        return Address(value[0], value[1], value[2], value[3])
        # return Address(value[0], value[1], value[2], value[3], value[4])
