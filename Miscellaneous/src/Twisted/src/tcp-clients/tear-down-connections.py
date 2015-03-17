from twisted.internet import reactor, protocol

class MyDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        print "Connected to %s." % self.transport.getPeer().host
        self.transport.loseConnection()
        
class MyClientFactory(protocol.ClientFactory):
    protocol = MyDisconnectProtocol
    
    def clientConnectionLost(self, connector, reason):
        print "Lost connection: %s" % reason.getErrorMessage()
        reactor.stop( )

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed: %s" % reason.getErrorMessage()
        reactor.stop( )

reactor.connectTCP('www.google.com', 80, MyClientFactory())
reactor.run()
