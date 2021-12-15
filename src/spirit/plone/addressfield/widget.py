# -*- coding: utf-8 -*-

from spirit.plone.addressfield.interfaces import IAddressField
from spirit.plone.addressfield.interfaces import IAddressWidget
from z3c.form.browser.object import ObjectWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import NO_VALUE
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.schema import getFieldNames


@implementer(IAddressWidget)
class AddressWidget(ObjectWidget):

    klass = u"address-widget form-control px-4 py-2"

    @property
    def value(self):
        """This invokes updateWidgets on any value change e.g. update/extract."""
        return super(AddressWidget, self).value

    @value.setter
    def value(self, value):
        self._value = value
        self.updateWidgets()

        # ensure that we apply our new values to the widgets
        if value is not NO_VALUE:
            for name in getFieldNames(self.field.schema):
                if not self.subform.widgets.get(name):
                    # In case a field is hidden/readonly
                    continue
                self.applyValue(
                    self.subform.widgets[name],
                    value.get(name, NO_VALUE),
                )


@implementer(IFieldWidget)
@adapter(IAddressField, IFormLayer)
def AddressFieldWidget(field, request):
    return FieldWidget(field, AddressWidget(request))
