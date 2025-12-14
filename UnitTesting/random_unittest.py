import unittest
import random_guess

class TestGame(unittest.TestCase):
    
    def test_input_guess_correctly(self):      
        result = random_guess.run_guess(5,5)
        self.assertTrue(result)
        
    def test_input_guess_incorrectly(self):
        result = random_guess.run_guess(5, 7)
        self.assertFalse(result)
        
    def test_input_wrong_number(self):
        result = random_guess.run_guess(5, 12)
        self.assertFalse(result)
    
    
    
if __name__ == '__main__':
    unittest.main()
    