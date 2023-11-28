def printDiagonalTraversal(nums):
    result = []
    for i in range(len(nums)):
        result.append(nums[i][i])
    return result
