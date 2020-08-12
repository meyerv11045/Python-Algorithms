import unittest
from searching import *

arry = [54, 36, 9, 14, 45, 24, 3, 76]
arryTarget = 14
arryIndex = 3

sortedArry = [2,3,4,10,40]
sortedTarget = 10
sortedIndex = 3

class TestSearching(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search(arry,arryTarget),arryIndex)
    def test_binary_search(self):
        self.assertEqual(binary_search_iterative(sortedArry,sortedTarget),sortedIndex)
        self.assertEqual(binary_search_recursive(sortedArry,0,len(sortedArry)-1,sortedTarget),sortedIndex)
    def test_jumpy_search(self):
        self.assertEqual(jump_search(sortedArry,sortedTarget),sortedIndex)
    def test_interpolation_search(self):
        self.assertEqual(interpolation_search(sortedArry,0,len(sortedArry)-1,sortedTarget),sortedIndex)

if __name__ == '__main__':
    unittest.main()