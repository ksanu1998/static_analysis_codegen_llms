def count_rectangles(N, M):
    p_x = (N * (N - 1)) // 2
    p_y = (M * (M - 1)) // 2
    return p_x * p_y


N = 3
M = 6
print(count_rectangles(N, M))
