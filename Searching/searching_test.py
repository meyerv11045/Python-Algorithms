import unittest
from searching import linear_search, binary_search

class TestSearching(unittest.TestCase):
    def test_linear_search(self):
        arry = [54, 36, 9, 14, 45, 24, 3, 76]
        self.assertEqual(linear_search(14,arry),3)
    def test_binary_search(self):
        arry = [2,3,4,10,40]
        self.assertEqual(binary_search(10,arry),4)

if __name__ == '__main__':
    unittest.main()