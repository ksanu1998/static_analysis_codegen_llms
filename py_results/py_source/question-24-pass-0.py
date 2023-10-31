# Count of repeating digits in a given Number. 
def countRepeatingDigits(N): 
    # Initialize result 
    result = 0
    # Traverse the given number 
    for i in range(10): 
        # Check if the digit is repeating 
        if N % 10 == i: 
            # Increment result 
            result += 1
        # Divide the number by 10 
        N = N // 10
    # Return result 
    return result 
  
# Driver Code 
N = 1234567890
print("Number of repeating digits in", N, "is", countRepeatingDigits(N)) 

# Output:
# Number of repeating digits in 1234567890 is 3

# Time Complexity: O(logN)
# Space Complexity: O(1)