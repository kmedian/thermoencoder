import numpy as np


def thermo_encode_8(arr: np.ndarray) -> np.ndarray:
    """Thermometer Encoding for integers labels from 0 to 8

    Parameters:
    -----------
    arr : ndarray, list, tuple
        Ordinal variables as vector with integers from 0 to 8.
        It's assumed that ordinal labels (e.g. big, medium, small)
        have been converted to integers from 0 to 8 (e.g. 0=small,
        2=big, 1=medium)

    Returns:
    --------
    enc : ndarray
        Matrix with binary values. The function always returns 8 columns.
        An example:

            label   columns
              0     0 0 0 0  0 0 0 0
              1     1 0 0 0  0 0 0 0
              2     1 1 0 0  0 0 0 0
              3     1 1 1 0  0 0 0 0
             ...    ...
              8     1 1 1 1  1 1 1 1

    Acknowledgements:
    -----------------
    Code found at
        https://stackoverflow.com/a/49081131
    """
    a = np.array(arr, dtype=np.uint8)
    return np.fliplr(np.unpackbits((1 << a) - 1).reshape(-1, 8))
