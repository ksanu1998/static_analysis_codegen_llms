def findTriangles(n):
    num = n
    print(num, end=" ")
    print(num * (num - 4) * (num - 5) // 6)


n = 6
findTriangles(n)
