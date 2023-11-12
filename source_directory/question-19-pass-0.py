# Mode in a stream of integers ( running integers ). 
def findMode(a, n): 
    # Initialize result 
    res = 0
    # Initialize count of elements with value res 
    count = 1
    # Traverse the array 
    for i in range(1, n): 
        # If current element is same as previous element, 
        # increment count 
        if (a[i] == a[i - 1]): 
            count += 1
        # Else if current element is not same as previous 
        # element, then check if count is more than maxCount 
        # and update maxCount and result 
        else: 
            if (count > count): 
                count = 1
                res = a[i] 
    return res 

# Driver program to test above function 
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] 
n = len(a) 
print("Mode is", findMode(a, n)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to find the mode in a stream of integers 
# ( running integers ). 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to find the mode in a stream of integers 
# ( running integers ). 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to find the mode in a stream of integers 
# ( running integers ). 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to find the mode in a stream of integers 
# ( running integers ). 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to find the mode in a stream of integers 
# ( running integers ). 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to