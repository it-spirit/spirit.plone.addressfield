# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import spirit.plone.addressfield


class SpiritPloneAddressfieldLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=spirit.plone.addressfield)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "spirit.plone.addressfield:default")


SPIRIT_PLONE_ADDRESSFIELD_FIXTURE = SpiritPloneAddressfieldLayer()


SPIRIT_PLONE_ADDRESSFIELD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SPIRIT_PLONE_ADDRESSFIELD_FIXTURE,),
    name="SpiritPloneAddressfieldLayer:IntegrationTesting",
)


SPIRIT_PLONE_ADDRESSFIELD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SPIRIT_PLONE_ADDRESSFIELD_FIXTURE,),
    name="SpiritPloneAddressfieldLayer:FunctionalTesting",
)


SPIRIT_PLONE_ADDRESSFIELD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SPIRIT_PLONE_ADDRESSFIELD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="SpiritPloneAddressfieldLayer:AcceptanceTesting",
)
