from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from .thermo_encode import thermo_encode_8
from .thermo_decode import thermo_decode_max


class ThermoEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X: np.ndarray, y=None):
        # convert to numpy array
        if not hasattr(X, "shape"):
            X = np.array(X)
        # store the number of integer labels (=max(X))
        if len(X.shape) > 1:
            self.n_features = X.shape[1]
            self.n_labels = []
            for j in range(self.n_features):
                self.n_labels.append(int(np.max(X[:, j])))
        else:
            self.n_features = 1
            self.n_labels = [np.max(X)]
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        # convert to numpy array
        if not hasattr(X, "shape"):
            X = np.array(X)
        # encode
        if self.n_features == 1:
            return thermo_encode_8(X)[:, :self.n_labels[0]]
        else:
            Z = []
            for j in range(self.n_features):
                Z.append(thermo_encode_8(X[:, j])[:, :self.n_labels[j]])
            return np.hstack(Z)

    def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
        # convert to numpy array
        if not hasattr(Z, "shape"):
            Z = np.array(Z)
        # decode
        X = np.empty(shape=(Z.shape[0], len(self.n_labels)), dtype=np.uint8)
        n0 = 0
        for j, n in enumerate(self.n_labels):
            n1 = n0 + n
            X[:, j] = thermo_decode_max(Z[:, n0:n1])
            n0 = n1
        return X
