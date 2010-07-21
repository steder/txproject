from twisted.trial import unittest
from twisted.web import server
from twisted.web.test import test_web

from default.web import root

class TestRootResource(unittest.TestCase):
    def setUp(self):
        self.r = root.Root()

    def test_create(self):
        r = root.Root()
        self.assertTrue(r is not None)

    def test_renderGet(self):
        """should get the login page"""
        result = self.r.render_GET(test_web.DummyRequest(['']))
        self.assertTrue(result == server.NOT_DONE_YET)
        return self.r.d
        
