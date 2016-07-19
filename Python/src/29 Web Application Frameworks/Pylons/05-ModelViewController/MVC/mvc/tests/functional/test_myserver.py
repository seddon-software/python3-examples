from mvc.tests import *

class TestMyserverController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='myserver', action='index'))
        # Test response...
