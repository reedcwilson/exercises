def spiral_matrix(size):
    '''fill in the matrix while rotating'''
    m = [[0] * size for _ in range(size)]
    trans_x, trans_y = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, v = 0, -1, 1
    for i in range(size + size - 1):
        for _ in range((size + size - i) // 2):
            x, y = x + trans_x[i % 4], y + trans_y[i % 4]
            m[x][y] = v
            v += 1
    return m
