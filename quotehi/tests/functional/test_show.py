from quotehi.tests import *

class TestShowController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='show', action='index'))
        # Test response...
