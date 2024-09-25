import numpy as np

def calculate(numbers):
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")

    else:
        array = np.array(numbers)
        matrix = np.reshape(array, (3, 3))
        
        mean_row = matrix.mean(axis=1)
        mean_col = matrix.mean(axis=0)
        mean_flat = matrix.mean()

        var_row = matrix.var(axis=1)
        var_col = matrix.var(axis=0)
        var_flat = matrix.var()

        std_row = matrix.std(axis=1)
        std_col = matrix.std(axis=0)
        std_flat = matrix.std()

        max_row = matrix.max(axis=1)
        max_col = matrix.max(axis=0)
        max_flat = matrix.max()

        min_row = matrix.min(axis=1)
        min_col = matrix.min(axis=0)
        min_flat = matrix.min()

        sum_row = matrix.sum(axis=1)
        sum_col = matrix.sum(axis=0)
        sum_flat = matrix.sum()

        return {
            'mean': [list(mean_col), list(mean_row), mean_flat], 
            'variance': [list(var_col), list(var_row), var_flat], 
            'standard deviation': [list(std_col), list(std_row), std_flat], 
            'max': [list(max_col), list(max_row), max_flat], 
            'min': [list(min_col), list(min_row), min_flat], 
            'sum': [list(sum_col), list(sum_row), sum_flat],
        }

