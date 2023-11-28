# Non. 
def findPrimes(arr, n): 
    # Initialize all array elements as prime 
    isPrime = [True for i in range(n)] 
  
    # Update isPrime array (reject all multiples of a prime) 
    for i in range(2, n): 
        if isPrime[i]: 
            for j in range(i*i, n, i): 
                isPrime[j] = False
  
    # Print all prime numbers 
    for i in range(n): 
        if isPrime[i]: 
            print(i) 
  
# Driver program to test above function 
arr = [10, 15, 20, 25, 30] 
n = len(arr) 
findPrimes(arr, n) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
