import unittest
from thermoencoder import thermo_decode_max
import numpy as np
import numpy.testing as npt


class Test_thermo_decode_max(unittest.TestCase):

    def test1(self):
        expected = np.array([2], dtype=np.uint8)
        decoded = thermo_decode_max([1, 1, 0])  # 1 sample input
        npt.assert_array_equal(decoded, expected)

    def test2(self):
        expected = np.array([2], dtype=np.uint8)
        decoded = thermo_decode_max([[1, 1, 0]])  # list of samples
        npt.assert_array_equal(decoded, expected)

    def test3(self):
        expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=np.uint8)
        decoded = thermo_decode_max(
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 1, 1, 1]])
        npt.assert_array_equal(decoded, expected)


# run
if __name__ == '__main__':
    unittest.main()
