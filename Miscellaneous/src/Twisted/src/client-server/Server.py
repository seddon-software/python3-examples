from twisted.internet import protocol, reactor, defer
from twisted.protocols import basic
from sys import stdout

class FingerProtocol(basic.LineReceiver):
    def onError(self):
        return "Internal error in server"
    
    def onCommand(self, name):
        self.transport.write(name + "\r\n")
        #self.transport.loseConnection()
        
    def lineReceived(self, user):
        stdout.write("user:" + user)
        defer = self.factory.getUser(user)
        defer.addErrback(self.onError)
        defer.addCallback(self.onCommand)

class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, args): self.users = args

    def getUser(self, user):
        return defer.succeed(self.users.get(user, "No such user"))

names = {
         "chris":"Chris is working at Cisco",
         "sue":  "Sue is working at Sun"
        }
reactor.listenTCP(1079, FingerFactory(names))
reactor.run()
