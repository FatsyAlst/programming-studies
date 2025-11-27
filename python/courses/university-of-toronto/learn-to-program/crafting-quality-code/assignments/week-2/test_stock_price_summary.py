import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_positive_and_negative_numbers(self):
        """Test stock_price_summary with mixed gains and losses.
        
        Tests lists containing both positive (gains) and negative (losses)
        values, including zeros. Verifies correct separation and summation.
        """
        self.assertEqual(a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]), (0.14, -0.17))
        self.assertEqual(a1.stock_price_summary([1.5, -2.0, 3.0, -1.5]), (4.5, -3.5))

    def test_only_gains(self):
        """Test stock_price_summary with only positive values.
        
        When all price changes are gains, losses should be 0.
        Tests single and multiple gain scenarios.
        """
        self.assertEqual(a1.stock_price_summary([5.0]), (5.0, 0))
        self.assertIn(a1.stock_price_summary([0.1, 0.2, 0.3]), [(0.6, 0), (0.6, 0.0)])

    def test_only_losses(self):
        """Test stock_price_summary with only negative values.
        
        When all price changes are losses, gains should be 0.
        Tests single and multiple loss scenarios.
        """
        self.assertIn(a1.stock_price_summary([-0.1, -0.2, -0.3]), [(0, -0.6), (0.0, -0.6)])
        self.assertEqual(a1.stock_price_summary([-10.0]), (0, -10.0))
    
    def test_empty_list(self):
        """Test stock_price_summary with an empty list.
        
        An empty list should return (0, 0) for gains and losses.
        """
        self.assertEqual(a1.stock_price_summary([]), (0, 0))
    
    def test_all_zero(self):
        """Test stock_price_summary with zeros mixed with other values.
        
        Zeros should be treated as losses (no effect on either sum).
        Verifies correct handling when zeros are interspersed.
        """
        self.assertEqual(a1.stock_price_summary([0, 0.5, 0, -0.5, 0]), (0.5, -0.5))

if __name__ == '__main__':
    unittest.main(exit=False)
