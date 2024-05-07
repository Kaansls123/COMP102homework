from Agecheck import agecheck

import unittest

# Assume that the constants and agecheck function have been imported or defined here

class TestAgeCheck(unittest.TestCase):
    def test_1(self):
        # Test for young drivers with low experience
        self.assertEqual(agecheck(23, 2), 4)  # 2 * 2 = 4
    
    def test_2(self):
        # Test for young drivers with more experience than minimum
        self.assertEqual(agecheck(23, 3), 2)  # Only age multiplier applies
    
    def test_3(self):
        # Test for older drivers with experience within limit
        self.assertEqual(agecheck(50, 5), 1)  # Only older age multiplier applies
    
    def test_4(self):
        # Test for older drivers exceeding experience limit
        self.assertEqual(agecheck(50, 6), 1)  # No multiplier applies
    
    def test_5(self):
        # Test for drivers older than 70 but not elderly
        self.assertEqual(agecheck(75, 3), 1.5)  # Older but not elderly multiplier
    
    def test_6(self):
        # Test for elderly drivers
        self.assertEqual(agecheck(81, 4), 2)  # Elderly multiplier
    
    def test_7(self):
        # Test for ages and experiences not explicitly handled
        self.assertEqual(agecheck(35, 7), 1)  # Default case with no multiplier
    
    def test_8(self):
        # Test boundaries for age and experience
        self.assertEqual(agecheck(25, 2), 4)  # Boundary of young driver with low experience
        self.assertEqual(agecheck(70, 5), 1)  # Boundary of older driver limit
        self.assertEqual(agecheck(80, 0), 1.5)  # Boundary of elderly age limit

if __name__ == "__main__":
    unittest.main()
