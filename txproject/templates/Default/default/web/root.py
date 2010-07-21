#-*- test-case-name: default.test.test_web -*-
import os

from twisted.python import log
from twisted.internet import defer, reactor
from twisted.web import http, resource, server, static

from default import settings


class Root(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
        self.putChild("static", static.File("default/static"))

    def _failed(self, reason):
        print "_failed:", reason
        log.err(reason)
        return http.Response(
            code=500,
            headers=None,
            stream=reason.getErrorMessage()
        )

    def _got(self, result, request):
        print "_got:", result, request
        request.setResponseCode(http.OK)
        request.write(result)
        request.finish()

    def getStaticFile(self, deferred):
        print "getStaticFile", deferred
        filepath = os.path.join(settings.default_root.path, "default/static/root.html")
        print "opening file:", filepath
        template = open(filepath, "r")
        print "opened file"
        contents = template.read()
        print "calling back:", contents
        deferred.callback(contents)
        print "called back"

    def render_GET(self, request):
        self.d = defer.Deferred()
        self.d.addCallback(self._got, request)
        self.d.addErrback(self._failed)
        reactor.callLater(0.1, self.getStaticFile, self.d)
        print "returning server.NOT_DONE_YET"
        return server.NOT_DONE_YET

    def getChild(self, path, request):
        if path == "":
            return self
        return resource.Resource.getChild(self, path, request)
