from twisted.python import failure
from twisted.trial import unittest

from default import server

class TestDefaultServer(unittest.TestCase):
    def setUp(self):
        portNumber = 6666
        self.server = server.DefaultServer(portNumber)
        
    def test_serverName(self):
        self.assertEqual(None, self.server.name
                         )

class TestDefaultServerStart(unittest.TestCase):
    def setUp(self):
        portNumber = 6666
        self.server = server.DefaultServer(portNumber)
        def _fakeServiceCallback(result):
            return result
        self.server._cbStarted = _fakeServiceCallback

    def tearDown(self):
        d = self.server.stopService()
        return d

    def _startSuccess(self, result):
        print "test_server._startSuccess:", result
        self.assertEqual(True, result, "Expect server start to return true result")
        return result

    def _startShouldNotFail(self, failure):
        print failure
        self.fail("start should succeed!")
        return failure

    def _startShouldNotSucceed(self, result):
        self.fail("Start shouldn't succeed!")

    def _startShouldFail(self, failure):
        self.assertTrue(failure is not None)

    def test_startService(self):
        d = self.server.startService()
        d.addCallbacks(callback=self._startSuccess,
                       errback=self._startShouldNotFail)
        return d

    def test_startServiceFails(self):
        def fakeStart(d):
            d.errback(failure.Failure(Exception("Some exception occured while starting the service")))
        self.server.startupHook = fakeStart
        d = self.server.startService()
        d.addCallbacks(callback=self._startShouldNotSucceed,
                       errback=self._startShouldFail)
        return d
        

