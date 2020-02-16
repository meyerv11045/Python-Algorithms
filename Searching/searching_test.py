import unittest
from searching import linear_search, binary_search_iterative,binary_search_recursive

class TestSearching(unittest.TestCase):
    def test_linear_search(self):
        arry = [54, 36, 9, 14, 45, 24, 3, 76]
        self.assertEqual(linear_search(14,arry),3)
    def test_binary_search(self):
        arry = [2,3,4,10,40]
        self.assertEqual(binary_search_iterative(10,arry),3)
        self.assertEqual(binary_search_recursive(10,arry,0,len(arry)-1),3)

if __name__ == '__main__':
    unittest.main()