from twisted.internet import reactor
from twisted.web import http

class MyRequestHandler(http.Request):
    def getFile(self, fileName):
        fileName = fileName.lstrip("/")
        fileName = "data/" + fileName
        print "fileName: " + fileName        
        f = open(fileName, "r")
        return f
        
    def process(self):
        try:
            f = self.getFile(self.path)
            
            for line in f:
                self.write(line)
        except:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Page not found</h1>")
        
        self.finish()
        

class MyPageProtocol(http.HTTPChannel):
    requestFactory = MyRequestHandler

class MyFactory(http.HTTPFactory):
    protocol = MyPageProtocol

reactor.listenTCP(16000, MyFactory( ))
reactor.run( )