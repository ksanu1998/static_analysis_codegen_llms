# Count of integers up to N which represent a Binary number. 
def countBinaries(N): 
    # Initialize result 
    result = 0
    # Initialize a boolean array to store 
    # whether a digit has been used or not 
    used = [False] * (N + 1)