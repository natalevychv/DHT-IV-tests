import unittest
import proposed_N3
import proposed_N4
import proposed_N5
import proposed_N6
import proposed_N7
import proposed_N8
import computeDHT_IVmatrix
import numpy as np


class Tests(unittest.TestCase):

    def test_n3(self):
        result = np.array(proposed_N3.proposed_N3(), dtype=np.float64)
        expected = np.array(computeDHT_IVmatrix.compute_DHT_IV_matrix(3), dtype=np.float64)
        np.testing.assert_array_almost_equal(result, expected, decimal=5)

    def test_n4(self):
        result = np.array(proposed_N4.proposed_N4(), dtype=np.float64)
        expected = np.array(computeDHT_IVmatrix.compute_DHT_IV_matrix(4), dtype=np.float64)
        np.testing.assert_array_almost_equal(result, expected, decimal=5)

    def test_n5(self):
        result = np.array(proposed_N5.proposed_N5(), dtype=np.float64)
        expected = np.array(computeDHT_IVmatrix.compute_DHT_IV_matrix(5), dtype=np.float64)
        np.testing.assert_array_almost_equal(result, expected, decimal=5)

    def test_n6(self):
        result = np.array(proposed_N6.proposed_N6(), dtype=np.float64)
        expected = np.array(computeDHT_IVmatrix.compute_DHT_IV_matrix(6), dtype=np.float64)
        np.testing.assert_array_almost_equal(result, expected, decimal=5)

    def test_n7(self):
        result = np.array(proposed_N7.proposed_N7(), dtype=np.float64)
        expected = np.array(computeDHT_IVmatrix.compute_DHT_IV_matrix(7), dtype=np.float64)
        np.testing.assert_array_almost_equal(result, expected, decimal=5)

    def test_n8(self):
        result = np.array(proposed_N8.proposed_N8(), dtype=np.float64)
        expected = np.array(computeDHT_IVmatrix.compute_DHT_IV_matrix(8), dtype=np.float64)
        np.testing.assert_array_almost_equal(result, expected, decimal=5)


if __name__ == '__main__':
    unittest.main()
