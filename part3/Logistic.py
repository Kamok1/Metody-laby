import numpy as np
from typing import Callable, Optional, Dict, List
from sklearn.metrics import accuracy_score


def ce_loss(y: np.ndarray, p: np.ndarray, eps: float = 1e-15) -> float:
    p = np.clip(p, eps, 1 - eps)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

def ce_grad(y: np.ndarray, p: np.ndarray) -> np.ndarray:
    return p - y

class CustomLogisticRegression:
    def __init__(self,lr: float = 0.05,epochs: int = 200,batch_size: int = 64,l1: float = 0.0,l2: float = 0.0,
                 loss_fn: Callable[[np.ndarray, np.ndarray], float] = ce_loss,grad_fn: Callable[[np.ndarray, np.ndarray], np.ndarray] = ce_grad,
                 seed: int = 0, verbose: bool = False,
    ):
        self.lr = lr
        self.epochs = epochs
        self.batch_sz = batch_size
        self.l1 = l1
        self.l2 = l2
        self.loss_fn = loss_fn
        self.grad_fn = grad_fn
        self.seed = seed
        self.verbose = verbose
        self.w_: Optional[np.ndarray] = None
        self.b_: float = 0.0
        self.history: Dict[str, List[float]] = {}

    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-z))

    def _init_params(self, n_features: int):
        rng = np.random.default_rng(self.seed)
        self.w_ = rng.normal(scale=0.01, size=n_features)
        self.b_ = 0.0

    def fit(
        self, X_train: np.ndarray,y_train: np.ndarray,X_val: Optional[np.ndarray] = None, y_val: Optional[np.ndarray] = None,
        X_test: Optional[np.ndarray] = None, y_test: Optional[np.ndarray] = None,
    ) -> "CustomLogisticRegression":
        m, n = X_train.shape
        self._init_params(n)
        rng = np.random.default_rng(self.seed)

        Htr, Hval, Hte = [], [], []

        for ep in range(self.epochs):
            perm = rng.permutation(m)
            for start in range(0, m, self.batch_sz):
                idx = perm[start : start + self.batch_sz]
                Xb, yb = X_train[idx], y_train[idx]

                z = Xb @ self.w_ + self.b_
                p = self._sigmoid(z)
                grad = (Xb.T @ self.grad_fn(yb, p)) / len(yb)
                grad += self.l2 * 2 * self.w_
                grad += self.l1 * np.sign(self.w_)
                self.w_ -= self.lr * grad
                self.b_ -= self.lr * self.grad_fn(yb, p).mean()

            p_tr  = self._sigmoid(X_train @ self.w_ + self.b_)
            Htr.append(self.loss_fn(y_train, p_tr))
            if X_val is not None:
                p_val = self._sigmoid(X_val @ self.w_ + self.b_)
                Hval.append(self.loss_fn(y_val, p_val))
            if X_test is not None:
                p_te  = self._sigmoid(X_test @ self.w_ + self.b_)
                Hte.append(self.loss_fn(y_test, p_te))

            if self.verbose and (ep == 0 or (ep + 1) % 20 == 0):
                msg = f"Epoch {ep+1:3d}/{self.epochs}  train_loss={Htr[-1]:.4f}"
                if Hval:
                    msg += f"  val_loss={Hval[-1]:.4f}"
                print(msg)

        self.history = {"train": Htr, "val": Hval, "test": Hte}
        return self


    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self._sigmoid(X @ self.w_ + self.b_)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        return (self.predict_proba(X) >= threshold).astype(int)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        return accuracy_score(y, self.predict(X))

    def get_params(self) -> Dict[str, float]:
        return {
            "lr": self.lr,
            "epochs": self.epochs,
            "batch_size": self.batch_sz,
            "l1": self.l1,
            "l2": self.l2,
            "seed": self.seed,
            "verbose": self.verbose,
            "loss_fn": self.loss_fn,
            "grad_fn": self.grad_fn,
        }

    def set_params(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self
