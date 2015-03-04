from navigation.tests import *

class TestRotateController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='rotate', action='index'))
        # Test response...
