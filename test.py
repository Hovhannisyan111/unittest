from script import *
import unittest

class Test(unittest.TestCase):
    def test_sorted(self):
        self.assertTrue(is_sorted([1,2,3,4,5]))
        self.assertFalse(is_sorted([3,1,5,2]))
    
    def test_anagrams(self):
        self.assertTrue(are_anagrams("kut", "tuk"))
        self.assertFalse(are_anagrams("are", "tea"))
    
    def test_merge(self):
        self.assertEqual(merge_sorted_lists([7,9,11], [6,8,10,12]), [6,7,8,9,10,11,12])

if __name__ == "__main__":
    unittest.main()
