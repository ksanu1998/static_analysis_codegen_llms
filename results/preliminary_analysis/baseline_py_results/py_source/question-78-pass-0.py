# Find the sum of the first Nth Centered Tridecagonal Numbers. 
def Centered_tridecagonal_num(n): 
    return (n * (n + 1) * (2 * n + 1)) / 6 
  
# Driver Code 
n = 10
print("Sum of the first", n, "Centered Tridecagonal Numbers is", 
      Centered_tridecagonal_num(n)) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 