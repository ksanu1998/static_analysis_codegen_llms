# Count of elements not divisible by any other elements of Array. 
def count(a, n): 
    count = 0
    for i in range(n): 
        if a[i]!= 0: 
            count += 1
    return count 
  
# Function to find the number of elements that are 
# divisible by all other elements of Array. 
def find(a, n): 
    count = 0
    for i in range(n): 
        if a[i]!= 0: 
            count += 1
    return count 
