def bomb_required(n):
    print(n + n // 2)
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    for i in range(1, n + 1, 2):
        print(i, end=" ")
    for i in range(2, n, 2):
        print(i, end=" ")


bomb_required(3)
