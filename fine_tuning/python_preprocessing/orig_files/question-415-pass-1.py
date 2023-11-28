def offeringNumber(n, templeHeight):
    for i in range(n):
        left = 0
        right = 0
        for j in range(i - 1, -1, -1):
            if (templeHeight[j] < templeHeight[j + 1]):
                left += 1
            else:
                break
        for j in range(i + 1, n):
            if (templeHeight[j] < templeHeight[j - 1]):
                right += 1
            else:
                break
        sum += max(right, left) + 1
    return sum


arr1 = [1, 2, 2]
print(offeringNumber(3, arr1))
arr2 = [1, 4, 3, 6, 2, 1]
print(offeringNumber(6, arr2))
