# Find the length of largest subarray in which all elements are Autobiographical Numbers. 
def isAutoBiographyNum(number): 
    if number == 0: 
        return True
    if number < 0: 
        return False
    if number % 10 == 0: 
        return False
    return isAutoBiographyNum(number//10) 
  
def longestAutobiographyNum(arr, n): 
    max_len = 0
    for i in range(n): 
        if isAutoBiographyNum(arr[i]): 
            j = i 
            while j < n and arr[j] == arr[i]: 
                j += 1
            max_len = max(max_len, j - i) 
            i = j - 1
    return max_len 
  
# Driver Code 
arr = [12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890] 
n = len(arr) 
print("Length of the longest Autobiographical Number is", longestAutobiographyNum(arr, n)) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 













































































































































































