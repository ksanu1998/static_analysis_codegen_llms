def find_Winner(arr, N):
    Q = [0] * N
    for i in range(N):
        Q[i] = []
    M = len(arr)
    for i in range(M):
        Len = len(arr[i])
        for j in range(Len):
            Q[i].append(ord(arr[i][j]) - 1)
    player = 0
    while (len(Q[player]) > 0):
        nextPlayer = Q[player][0] - ord('0')
        del Q[player][0]
        player = nextPlayer
    print("Player", (player + 1))


N = 3
arr = ["323", "2", "2"]
find_Winner(arr, N)
