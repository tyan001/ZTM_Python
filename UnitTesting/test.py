import unittest
import main

class TestMain(unittest.TestCase):
    
    def setUp(self):
        print('testing a function')
    
    
    def test_foo(self):
       
        test_param = 10
        result = main.foo(test_param)
        self.assertEqual(result, 15)
        
    # def test_foo2(self):
    #     test_param = "10"
    #     result = main.foo(test_param)
    #     self.assertIsInstance(result,TypeError)
        
    def test_foo2(self):
        test_param = "10"
        result = main.foo(test_param)
        self.assertEqual(result, 'please enter a number')
        
    def test_foo3(self):
        test_param = None
        result = main.foo(test_param)
        self.assertEqual(result, 'please enter a number')
        
    
    def tearDown(self):
        print('Cleaning up')
        
    
if __name__ == '__main__':
    unittest.main()    