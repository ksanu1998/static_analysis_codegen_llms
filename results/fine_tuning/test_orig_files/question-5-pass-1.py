def sameProductQuadruples(nums, N):

def sameProductQuadruples(nums, N):
    count = 0
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                if nums[i] * nums[j] == nums[k] * nums[N-1]:
                    count += 1
    return count
