# -*- coding: utf-8 -*-
from imioweb.core.testing import IMIOWEB_CORE_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class TestView(unittest.TestCase):
    layer = IMIOWEB_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_geojson_popup_view(self):
        # create taxonomy
        # create document with taxonomy value
        # get value from popup view with "brained" document
        self.assertTrue(True)
