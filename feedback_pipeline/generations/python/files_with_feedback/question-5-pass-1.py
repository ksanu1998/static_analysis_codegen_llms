def sameProductQuadruples(nums, N):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if nums[i] * nums[j] == nums[k] * nums[k+1]:
                    count += 1
    return count
