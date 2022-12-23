import unittest
from unittest.mock import Mock

from main import get_roots, get_roots_biquadratic

class MOCKtestGetRoots(unittest.TestCase):
	def testGetRoots(self):
		mockRoot = Mock(return_value=5)
		get_roots_biquadratic(get_roots(mockRoot(), 5, 5))

if __name__ == "__main__":
	unittest.main()
