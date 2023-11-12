# Count pairs in an array containing at least one even value. 
def CountPairs(arr, n): 
    count = 0
    for i in range(n): 
        for j in range(i+1, n): 
            if (arr[i] % 2 == 0 or arr[j] % 2 == 0): 
                count += 1
    return count 
  
# Driver code 
arr = [1, 2, 3, 4, 5, 6] 
n = len(arr) 
print("Count of pairs with at least one even value is", 
      CountPairs(arr, n)) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 