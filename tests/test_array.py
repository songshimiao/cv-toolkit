import numpy as np


def test_numpy_array():
    arr = np.arange(5)
    assert arr.tolist() == [0, 1, 2, 3, 4]
    assert arr.sum() == 10
