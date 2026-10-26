# Cell 1
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    if not a:
        return []
    
    count_col = len(b)
    
    for row in a: 
        if len(row) != count_col:
            return -1
        
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    return [sum(x * y for x, y in zip(row, b)) for row in a]