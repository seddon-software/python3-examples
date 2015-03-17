from twisted.internet import reactor

def printMessage(msg):
    print msg

def stopReactor():
    print "Stopping reactor"
    reactor.stop( )

reactor.callLater(1, printMessage, "called after 1 second")
reactor.callLater(1, printMessage, "called after 1 second")
reactor.callLater(1, printMessage, "called after 1 second")
reactor.callLater(10, printMessage, "called after 10 seconds")
reactor.callLater(24, printMessage, "called after 24 seconds")
reactor.callLater(25, stopReactor)

print "Running the reactor..."
reactor.run( )
print "Reactor stopped."

reactor.callLater(2, printMessage, "called after 2 seconds")
reactor.callLater(5, stopReactor)
reactor.run()
