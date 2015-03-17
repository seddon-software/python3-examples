from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientCreator
from twisted.internet.interfaces import IReactorThreads
from sys import stdout
from sys import stdin
import time


class Greeter(Protocol):
    def dataReceived(self, data):
        stdout.write(data)
        stdout.write("Input name: ")
        stdout.flush()

    def sendMessage(self, msg):
        self.transport.write(msg + "\r\n")

def gotProtocol(p):
    p.sendMessage("chris")
    reactor.callLater(5, p.sendMessage, "sue")
    reactor.callInThread(getName, p)
    #reactor.callLater(12, p.transport.loseConnection)



def getName(p):
    while True:
        name = raw_input()
        stdout.write(name + ": ")
        p.sendMessage(name)

c = ClientCreator(reactor, Greeter)
c.connectTCP("localhost", 1079).addCallback(gotProtocol)
#reactor.callInThread(aSillyBlockingMethod2, "3 seconds have passed")
reactor.run()



1
