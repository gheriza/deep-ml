import numpy as np

def rmse(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")

    if y_true.size == 0:
        raise ValueError("Arrays must not be empty")

    rmse_res = np.sqrt(np.mean((y_true - y_pred) ** 2))

    return round(float(rmse_res), 3)