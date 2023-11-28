# Count of integers up to N which represent a Binary number. 
from math import *


def countBinaries(N): 
    return int(floor(N * log2(N + 1))) 


# Driver Code 
if __name__ == '__main__': 
    N = 10
    print("Count of integers up to N which represent a Binary number is",
          countBinaries(N)) 


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# 1. Write a program to find the number of integers up to N which are divisible by 5. 

# 2. Write a program to find the number of integers up to N which are divisible by 5 and 7. 

# 3. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11. 

# 4. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11 and 13. 

# 5. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11 and 13 and 17. 

# 6. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11 and 13 and 17 and 19. 

# 7. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11 and 13 and 17 and 19 and 23. 

# 8. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11 and 13 and 17 and 19 and 23 and 29. 

# 9. Write a program to find the number of integers up to N which are divisible by 5 and 7 and 11 and 13 and 17 and 19 and 23 and 29 and 31. 

# 10