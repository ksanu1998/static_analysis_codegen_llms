# Sum of first N natural numbers with alternate signs. 
def alternatingSumOfFirst_N(N): 
    sum = 0
    for i in range(1, N+1): 
        if i % 2 == 0: 
            sum += i 
        else: 
            sum -= i 
    return sum 
  
# Driver Code 
N = 10
print("Sum of first", N, "natural numbers with alternate signs is", 
      alternatingSumOfFirst_N(N))