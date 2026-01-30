import multiply
import unittest

class testMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply.multiply(2,4), 8)

    def test_multiply_negative(self):
        self.assertEqual(multiply.multiply(-2,3), -6)

    def test_multiply_negative2(self):
        self.assertNotEqual(multiply.multiply(-2,-3), -6)

if __name__ == '__main__':
    unittest.main()
