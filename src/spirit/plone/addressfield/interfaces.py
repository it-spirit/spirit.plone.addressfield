# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from spirit.plone.addressfield import _
from z3c.form.interfaces import IWidget
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema.interfaces import IObject


class ISpiritPloneAddressfieldLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAddressField(IObject):
    pass


class IAddress(Interface):
    """Schema for addresses."""

    address = schema.TextLine(
        required=False,
        title=_(
            "address_label_address",
            default="Address",
        ),
    )

    postcode = schema.TextLine(
        required=False,
        title=_(
            "address_label_postcode",
            default="Postcode",
        ),
    )

    place = schema.TextLine(
        required=False,
        title=_(
            "address_label_place",
            default="City",
        ),
    )

    region = schema.TextLine(
        required=False,
        title=_(
            "address_label_region",
            default="Region",
        ),
    )

    country = schema.Choice(
        default="DE",
        required=False,
        title=_(
            "address_label_country",
            default="Country",
        ),
        vocabulary="spirit.plone.addressfield.available_countries",
    )


class IAddressWidget(IWidget):
    pass
