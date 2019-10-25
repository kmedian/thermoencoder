import numpy as np


def thermo_decode_max(Xin: np.ndarray, copy: bool = True) -> np.ndarray:
    # copy input
    X = np.array(Xin, copy=copy)
    # assume a single vector to be 1 sample
    if len(X.shape) == 1:
        X = np.array([X])
    # Assume int labels to range from 0 to M
    # wheras M the number of columns
    n_targets = X.shape[1]
    for j in range(n_targets - 1, 0, -1):
        idx = X[:, j].astype(bool)
        X[idx, j - 1] = 1
    return X.sum(axis=1).astype(np.uint8)
