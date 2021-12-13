# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from spirit.plone.addressfield import _
from spirit.plone.addressfield.field import AddressField
from zope.interface.declarations import provider

import pkg_resources


try:
    pkg_resources.get_distribution("plone.app.multilingual")
except pkg_resources.DistributionNotFound:
    HAS_PAM = False
else:
    from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
    from zope.interface import alsoProvides

    HAS_PAM = True


@provider(IFormFieldProvider)
class IAddressBehavior(model.Schema):
    """Add address information to content items."""

    address = AddressField(
        required=False,
        title=_(
            "address_behavior_label_address",
            default="Address",
        ),
    )


if HAS_PAM:
    alsoProvides(IAddressBehavior["address"], ILanguageIndependentField)
