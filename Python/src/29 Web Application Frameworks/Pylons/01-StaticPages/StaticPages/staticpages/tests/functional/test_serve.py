from staticpages.tests import *

class TestServeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='serve', action='index'))
        # Test response...
