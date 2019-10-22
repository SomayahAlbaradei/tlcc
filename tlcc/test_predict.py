import os
from tlcc.predict import _colony_count

dir = os.path.dirname(os.path.abspath(__file__))

class TestTLCCwebapp(object):

    def test_colony_count_file(self):
        r, _ = _colony_count(dir + '/../data/1.jpg')
        assert r == 673 or r == 668
