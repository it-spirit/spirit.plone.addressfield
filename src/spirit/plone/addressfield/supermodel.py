# -*- coding: utf-8 -*-

from plone.supermodel.exportimport import BaseHandler
from spirit.plone.addressfield.field import AddressField


AddressFieldHandler = BaseHandler(AddressField)
