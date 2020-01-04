import unittest
from searching import linear_search

class TestSearching(unittest.TestCase):
    def test_linear_search(self):
        arry = [54, 36, 9, 14, 45, 24, 3, 76]
        self.assertEqual(linear_search(14,arry),3)