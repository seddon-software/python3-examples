from twisted.protocols import basic
from twisted.internet import protocol, reactor

class MyEchoProtocol(basic.LineReceiver):
    def __init__(self):
            self.lines = []
            self.sentResponse = False

    def lineReceived(self, line):
        self.lines.append(line)
        if line:
            self.sentResponse = False
        else:
            if not self.sentResponse:
                self.sendResponse()

    def sendResponse(self):
        responseBody = "\r\n".join(self.lines)
        self.sendLine("HTTP/1.0 200 OK")
        self.sendLine("Content-Type: text/plain")
        self.sendLine("Content-Length: %i" % len(responseBody))
        self.sendLine("")
        self.transport.write(responseBody)
        self.transport.loseConnection()
        self.sentResponse = True


class MyFactory(protocol.ServerFactory):
    protocol = MyEchoProtocol

reactor.listenTCP(16000, MyFactory())
reactor.run()
