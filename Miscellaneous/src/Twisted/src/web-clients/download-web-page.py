from twisted.web import client
from twisted.internet import reactor
import sys

def printPage(data):
    print data
    reactor.stop( )

def printError(failure):
    print >> sys.stderr, "Error:", failure.getErrorMessage( )
    reactor.stop( )
    
url = "http://localhost:8080/mytest.html"
#url = "http://www.ibm.com:80"
deferred = client.getPage(url)
deferred.addCallback(printPage)
deferred.addErrback(printError)
reactor.run()
