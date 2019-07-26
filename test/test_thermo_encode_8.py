import unittest
from thermoencoder import thermo_encode_8
import numpy as np
import numpy.testing as npt


class Test_thermo_encode_8(unittest.TestCase):

    def test0(self):
        expected = np.array([[0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([0])
        npt.assert_array_equal(encoded, expected)

    def test1(self):
        expected = np.array([[1, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([1])
        npt.assert_array_equal(encoded, expected)

    def test2(self):
        expected = np.array([[1, 1, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([2])
        npt.assert_array_equal(encoded, expected)

    def test3(self):
        expected = np.array([[1, 1, 1, 0, 0, 0, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([3])
        npt.assert_array_equal(encoded, expected)

    def test4(self):
        expected = np.array([[1, 1, 1, 1, 0, 0, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([4])
        npt.assert_array_equal(encoded, expected)

    def test5(self):
        expected = np.array([[1, 1, 1, 1, 1, 0, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([5])
        npt.assert_array_equal(encoded, expected)

    def test6(self):
        expected = np.array([[1, 1, 1, 1, 1, 1, 0, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([6])
        npt.assert_array_equal(encoded, expected)

    def test7(self):
        expected = np.array([[1, 1, 1, 1, 1, 1, 1, 0]], dtype=np.uint8)
        encoded = thermo_encode_8([7])
        npt.assert_array_equal(encoded, expected)

    def test8(self):
        expected = np.array([[1, 1, 1, 1, 1, 1, 1, 1]], dtype=np.uint8)
        encoded = thermo_encode_8([8])
        npt.assert_array_equal(encoded, expected)

    def test_all(self):
        expected = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 1, 1, 1]],
            dtype=np.uint8)
        encoded = thermo_encode_8([0, 1, 2, 3, 4, 5, 6, 7, 8])
        npt.assert_array_equal(encoded, expected)


# run
if __name__ == '__main__':
    unittest.main()
