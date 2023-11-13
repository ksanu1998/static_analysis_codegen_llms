# Count of pairs having bit size at most X and Bitwise OR equal to X. 
def count_pairs(x): 
    global count 
    count = 0 
    for i in range(x + 1): 
        for j in range(i + 1): 
            if (i | j) == x: 
                count += 1 
    return count 
  
# Driver Code 
if __name__ == '__main__': 
    x = 10 
    print("Count of pairs having bit size at most", x, 
          "and Bitwise OR equal to", x, "is", 
          count_pairs(x)) 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is contributed by Rajat Mishra 
  
# This code is