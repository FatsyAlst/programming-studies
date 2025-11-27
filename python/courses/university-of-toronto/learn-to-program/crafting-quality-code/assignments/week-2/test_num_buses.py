import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_multiples_of_50(self):
        """Test num_buses with exact multiples of 50.
        
        When n is a multiple of 50, should return n // 50 buses.
        """
        self.assertEqual(a1.num_buses(50), 1)
        self.assertEqual(a1.num_buses(100), 2)
    
    def test_non_multiples_of_50(self):
        """Test num_buses with non-multiples of 50.
        
        When n is not a multiple of 50, should round up to the next bus.
        """
        self.assertEqual(a1.num_buses(39), 1)
        self.assertEqual(a1.num_buses(74), 2)
    
    def test_edge_cases(self):
        """Test num_buses with edge cases.
        
        Tests boundary conditions: 0 people (no buses needed) and
        large numbers to ensure the calculation scales correctly.
        """
        self.assertEqual(a1.num_buses(0), 0)
        self.assertEqual(a1.num_buses(1000), 20)


if __name__ == '__main__':
    unittest.main(exit=False)
