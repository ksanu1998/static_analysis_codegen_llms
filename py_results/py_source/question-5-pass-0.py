# Count of quadruples with product of a pair equal to the product of the remaining pair. 
def sameProductQuadruples(nums, N): 
    # Count of quadruples with product of a pair equal to the product of the remaining pair. 
    count = 0
    # Sort the array 
    nums.sort() 
  
    # Traverse the array from left to right 
    for i in range(N): 
        # Traverse the array from right to left 
        for j in range(i + 1, N): 
            # Traverse the array from right to left 
            for k in range(j + 1, N): 
                # Traverse the array from right to left 
                for l in range(k + 1, N): 
                    # If product of a pair is equal to the product of the remaining pair 
                    if (nums[i] * nums[j] == nums[k] * nums[l]): 
                        count += 1
    return count 
  
# Driver code 
nums = [1, 2, 3, 4, 5, 6] 
N = len(nums) 
print("Count of quadruples with product of a pair equal to the product of the remaining pair is", 
      sameProductQuadruples(nums, N)) 
  
# This code is contributed by Nikhil Kumar Singh 











































































































































































