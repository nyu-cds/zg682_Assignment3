import unittest
from parallel_sorter import inputNumSize, parallel_sorter
from mpi4py import MPI
import numpy as np

'''
test file
'''
class TestSorter(unittest.TestCase):

    def setUp(self):
        comm = MPI.COMM_WORLD
        self.rank = comm.Get_rank()
    def test_inputNumSize(self):
    """
    test if the input is right
    """
        if self.rank == 0:
            (size_,range_) = inputNumSize()
            self.assertIsInstance(size_, int)
            self.assertIsInstance(range_,int)

    def test_parallel_sorter(self):
    """
    test if the result is right?
    """
        result = parallel_sorter()
        if self.rank == 0:
            assert np.array_equal(result,sorted(result)), "Wrong Order"
            
        else:
            self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
