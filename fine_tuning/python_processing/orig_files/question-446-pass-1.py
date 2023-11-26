def printDiagonalTraversal(nums):
    m = len(nums)
    q = []
    q .append([0, 0])
    while (len(q) != 0):
        p = q[0]
        q .pop(0)
        print(nums[p[0]][p[1]], end=" ")
        if (p[1] == 0 and p[0] + 1 < m):
            q .append([p[0] + 1, p[1]])
        if (p[1] + 1 < len(nums[p[0]])):
            q .append([p[0], p[1] + 1])


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printDiagonalTraversal(arr)
