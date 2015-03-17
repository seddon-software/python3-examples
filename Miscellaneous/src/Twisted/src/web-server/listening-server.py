from twisted.internet import protocol, reactor

class MyProtocol(protocol.Protocol):
    pass

class MyFactory(protocol.ServerFactory):
    protocol = MyProtocol
    
reactor.listenTCP(15015, MyFactory())
reactor.listenTCP(15016, MyFactory())
reactor.listenTCP(15017, MyFactory())
reactor.run()
