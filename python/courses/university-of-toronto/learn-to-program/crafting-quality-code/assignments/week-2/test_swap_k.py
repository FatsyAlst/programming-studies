import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_k_is_zero(self):
        """Test swap_k when k is 0.
        
        When k=0, no elements should be swapped.
        The list should remain unchanged.
        """
        nums = [1, 2, 3, 4]
        a1.swap_k(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_is_len_k_divided_by_2_and_given_integer(self):
        """Test swap_k when k equals len(L) // 2.
        
        When k is half the list length, the entire first half should
        swap with the entire second half. Tests various list sizes.
        """
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [5, 6, 3, 4, 1, 2])
        
        nums = [1, 2, 3, 4]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [3, 4, 1, 2])
        
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])

    def test_odd_length_lists(self):
        """Test swap_k with odd-length lists.
        
        Verifies correct swapping when the list has an odd number of
        elements, leaving the middle element(s) in place.
        """
        nums = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [4, 5, 3, 1, 2])
        
        nums = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, [5, 2, 3, 4, 1])

    def test_small_list(self):
        """Test swap_k with the smallest possible list.
        
        Tests the minimum case: a 2-element list with k=1.
        Should swap the two elements.
        """
        nums = [1, 2]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, [2, 1])

if __name__ == '__main__':
    unittest.main(exit=False)
