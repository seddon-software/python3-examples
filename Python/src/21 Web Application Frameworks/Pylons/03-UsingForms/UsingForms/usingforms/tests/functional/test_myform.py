from usingforms.tests import *

class TestMyformController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='myform', action='index'))
        # Test response...
