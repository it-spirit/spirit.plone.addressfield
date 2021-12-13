# -*- coding: utf-8 -*-
"""Vocabularies for countries."""

from gocept.country.db import Country
from operator import itemgetter
from plone import api
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import pycountry


@implementer(IVocabularyFactory)
class AvailableCountriesVocabulary(object):
    """Return a list of available countries."""

    def __call__(self, context):
        request = getRequest()
        language = api.portal.get_current_language()

        countries = []
        for country in pycountry.countries:
            try:
                country_code = getattr(country, "alpha_2")
            except AttributeError:
                # Fallback for older pycountry versions
                country_code = getattr(country, "alpha2")
            title = translate(
                Country(country_code).name, context=request, target_language=language
            )
            countries.append((country_code, title))

        countries.sort(key=itemgetter(1))
        terms = [SimpleTerm(item[0], item[0], item[1]) for item in countries]
        return SimpleVocabulary(terms)


AvailableCountriesVocabularyFactory = AvailableCountriesVocabulary()
