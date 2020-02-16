import unittest
from sorting import bubble_sort,selection_sort,insertion_sort,merge_sort,quicksort

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        unsorted = [9,4,2,5,1]
        bubble_sort(unsorted)
        sortedd = [1,2,4,5,9]
        self.assertListEqual(unsorted,sortedd)
    def test_selection_sort(self):
        unsorted = [9,4,2,5,1]
        selection_sort(unsorted)
        sortedd = [1,2,4,5,9]
        self.assertListEqual(unsorted,sortedd)
    def test_insertion_sort(self):
        unsorted = [9,4,2,5,1]
        insertion_sort(unsorted)
        sortedd = [1,2,4,5,9]
        self.assertListEqual(unsorted,sortedd)
    def test_merge_sort(self):
        unsorted = [9,4,2,5,1]
        sortedd = [1,2,4,5,9]
        self.assertListEqual(merge_sort(unsorted),sortedd)
    def test_quicksort(self):
        unsorted = [9,4,2,5,1]
        sortedd = [1,2,4,5,9]
        self.assertListEqual(quicksort(unsorted),sortedd)

if __name__ == '__main__':
    unittest.main()