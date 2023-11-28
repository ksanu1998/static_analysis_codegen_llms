# Prefix Product Array. 
def prefixProduct(a, n): 
    # Initialize prefix[] 
    prefix = [0] * (n + 1) 
  
    # Compute prefix products 
    for i in range(1, n + 1): 
        prefix[i] = prefix[i - 1] * a[i - 1] 
  
    return prefix 
  
# Driver Code 
a = [1, 2, 3, 4, 5] 
n = len(a) 
prefix = prefixProduct(a, n) 
print("Prefix Products are:") 
for i in range(n): 
    print(prefix[i], end = " ") 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
  
# This code is contributed by Nikhil Kumar Singh(