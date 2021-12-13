# -*- coding: utf-8 -*-

from spirit.plone.addressfield.interfaces import IAddressField
from spirit.plone.addressfield.interfaces import IAddressWidget
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer_only


@implementer_only(IAddressWidget)
class AddressWidget(TextWidget):

    klass = u"address-widget"
    value = None

    def _default_value(self):
        return (None, None, None, None, None)

    def update(self):
        super(AddressWidget, self).update()
        if self.value is None and self.mode == "input":
            self.value = self._default_value()

    @property
    def id_input_address(self):
        return u"{0}_address".format(self.id)

    @property
    def id_input_postcode(self):
        return u"{0}_postcode".format(self.id)

    @property
    def id_input_place(self):
        return u"{0}_place".format(self.id)

    @property
    def id_input_region(self):
        return u"{0}_region".format(self.id)

    @property
    def id_input_country(self):
        return u"{0}_country".format(self.id)


@implementer(IFieldWidget)
@adapter(IAddressField, IFormLayer)
def AddressFieldWidget(field, request):
    return FieldWidget(field, AddressWidget(request))
