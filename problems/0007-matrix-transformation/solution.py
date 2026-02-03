import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[float]] | int:
    try:
        arr_A = np.array(A)
        arr_T = np.array(T)
        arr_S = np.array(S)

        # 1. Validate T is invertible (must be square and non-singular)
        # We try to invert it; if it fails, it's not invertible.
        inv_T = np.linalg.inv(arr_T)

        # 2. Validate S is invertible (must be square and non-singular)
        # We check shape and determinant.
        if arr_S.shape[0] != arr_S.shape[1] or np.isclose(np.linalg.det(arr_S), 0):
            return -1

        # 3. Calculate T^(-1) * A * S
        result_matrix = inv_T @ arr_A @ arr_S
        
        # Return as a standard Python list of lists
        return result_matrix.tolist()

    except np.linalg.LinAlgError:
        return -1
    except ValueError:
        # Handles dimension mismatches (e.g., A and T are incompatible shapes)
        return -1