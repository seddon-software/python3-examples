from twisted.internet import reactor, defer, protocol
import time

class CallbackAndDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.deferred.callback("Connected!")
        self.transport.loseConnection( )

class ConnectionTestFactory(protocol.ClientFactory):
    protocol = CallbackAndDisconnectProtocol

    def __init__(self):
        self.deferred = defer.Deferred( )

    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)

def testConnect(host, port):
    testFactory = ConnectionTestFactory( )
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred

def handleSuccess(result, port):
    print "Connected to port: " + str(port)
    reactor.stop()

def handleFailure(failure, port):
    print "Error connecting to port: " + str(port)
    print failure.getErrorMessage()
    reactor.stop()

def testConnection(host, port):
    connecting = testConnect(host, port)
    connecting.addCallback(handleSuccess, port)
    connecting.addErrback(handleFailure, port)
    reactor.run( )

#testConnection("localhost", 80)
testConnection("localhost", 8080)
#testConnection("localhost", 9090)
print "end of test"
