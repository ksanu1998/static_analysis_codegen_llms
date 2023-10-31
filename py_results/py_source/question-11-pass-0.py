# Minimum number of coins having value equal to powers of 2 required to obtain N. 
def count_setbit(N): 
    count = 0
    while N: 
        N &= (N - 1) 
        count += 1
    return count 
  
# Driver code 
N = 12
print(count_setbit(N)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# Python program to find the number of set bits in an integer 
# using bitwise operator 
  
# Function to count set bits in an integer 
def countSetBits(N): 
    count = 0
    while N: 
        N &= (N - 1) 
        count += 1
    return count 
  
# Driver code 
N = 12
print(countSetBits(N)) 