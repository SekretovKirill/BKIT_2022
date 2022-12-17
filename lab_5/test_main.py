import unittest
from unittest.mock import patch, Mock
from main import get_roots, check
import math

class TestRoots(unittest.TestCase):

    def test_roots_is_equal(self):
        self.assertEqual(get_roots(1,-7,4), [-2.524, 2.524, -0.792, 0.792])
        self.assertEqual(get_roots(1,-4,4), [-1.414, 1.414])
        self.assertEqual(get_roots(-4,40,0), [-0.0, -3.162, 3.162])
        self.assertEqual(get_roots(1,0,-16), [-2.0, 2.0])

    def test_string_root(self):
        self.assertRaises(TypeError, get_roots, '0000')
        self.assertRaises(TypeError, get_roots, 'True')
        self.assertRaises(TypeError, get_roots, [1,1])

if __name__ == '__main__':
    unittest.main()
