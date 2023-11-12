# Find count of numbers from 0 to n which satisfies the given equation for a value K. 
def findAns(a, b, n): 
    # Initialize result 
    result = 0
    # Find count of numbers from 0 to n which satisfies the given equation 
    for i in range(n + 1): 
        if (a * i + b) % n == 0: 
            result += 1
    return result 
  
# Driver code 
a = 2
b = 3
n = 10
print("Count of numbers from 0 to n which satisfies the given equation is",
      findAns(a, b, n)) 
  
# This code is contributed by Rajat Mishra 

















































































































































































































































































































































