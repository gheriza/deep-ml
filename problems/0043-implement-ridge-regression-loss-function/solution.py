import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    n = X.shape[0]

    predictions = X @ w
    mse = np.mean((y_true - predictions) ** 2)

    regularization = alpha * np.sum(w ** 2)

    return float(mse + regularization)