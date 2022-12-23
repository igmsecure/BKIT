import unittest

from main import get_roots, get_roots_biquadratic

class TestGetRoots(unittest.TestCase):
    def testGetRoots(self):
        self.assertEqual(get_roots_biquadratic(get_roots(4, -5, 1)), [1.0, -1.0, 0.5, -0.5])
        self.assertEqual(get_roots_biquadratic(get_roots(1, -2, -8)), [2.0, -2.0])
        self.assertEqual(get_roots_biquadratic(get_roots(1, 1, 1)), [])

    def testValue(self):
        with self.assertRaises(ValueError) as e:
            get_roots_biquadratic(get_roots(0, 33, 9))

    def testType(self):
        with (self.assertRaises(TypeError)) as e:
            get_roots_biquadratic(get_roots(7, "D", 4))

if __name__ == "__main__":
	unittest.main()