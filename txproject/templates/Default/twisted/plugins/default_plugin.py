from zope import interface

from twisted import plugin
from twisted.application import service
from twisted.python import usage

from default import server, settings


class Options(usage.Options):
    optParameters = (
        ('port', 'p', None, 'Port on which to listen.'),
    )


class DefaultServiceMaker(object):
    interface.implements(plugin.IPlugin, service.IServiceMaker)
    description = "Default"
    options = Options
    tapname = 'default'

    def makeService(self, options):
        """
        Return an instance of default.server.DefaultServer
        """
        port = settings.port

        if options['port'] is not None:
            port = int(options['port'])

        return server.DefaultServer(port)


serviceMaker = DefaultServiceMaker()
