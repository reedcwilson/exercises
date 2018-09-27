def saddle_points(matrix):
    columns = list(zip(*matrix))
    if len(matrix) != len(columns):
        raise ValueError('The matrix must be regular')
    return {
            (i, j)
            for j, row in enumerate(matrix)
            for i in range(len(row))
            if (all(matrix[i][j] >= n for n in matrix[i])
                and all(matrix[i][j] <= n for n in columns[j]))
    }
