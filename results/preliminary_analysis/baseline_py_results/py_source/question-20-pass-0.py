# Count of distinct numbers formed by shuffling the digits of a large number N. 
def modexp(x, n, m): 
    if n == 0: 
        return 1
    if n % 2 == 0: 
        return (modexp(x, n/2, m) * modexp(x, n/2, m)) % m 
    return (x * modexp(x, n-1, m)) % m 
 
def count_distinct(n): 
    # Count of distinct numbers formed by shuffling the digits of a large number N. 
    # The number N is represented as a string. 
    # The function returns the count of distinct numbers formed by shuffling the digits of N. 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the number of distinct numbers formed by shuffling the digits of N! 
    # The function uses the fact that the number of distinct numbers formed by shuffling the digits of a number N is equal to the