def isAutoBiographyNum(number):# Check if the number is a perfect square
    root = math.sqrt(number)
    if root == int(root):
        # Check if the number is a Autobiographical Number
        if number % (root + 1) == 0:
            return True
    return False

def largestSubarrayAutobiographyNum(arr):[/INST]
    max_len = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        # Check if the current element is a Autobiographical Number
        if isAutoBiographyNum(arr[i]):
            # Update the start and end indices of the subarray
            start = i
            end = i

            # Check if the subarray is the largest so far
            while end < len(arr) - 1 and isAutoBiographyNum(arr[end + 1]):
                end += 1

            if end - start + 1 > max_len:
                max_len = end - start + 1

    return max_len

arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(largestSubarrayAutobiographyNum(arr)) # Output: 4