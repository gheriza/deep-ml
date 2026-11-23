import numpy as np

def dice_score(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    denominator = np.sum(y_true == 1) + np.sum(y_pred == 1)

    if denominator == 0:
        return 0.0

    result = (2 * tp) / denominator
    return round(float(result), 3)