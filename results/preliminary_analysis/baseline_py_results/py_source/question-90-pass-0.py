# Find N numbers such that a number and its reverse are divisible by sum of its digits. 
def digit_sum(n): 
    sum = 0
    while (n > 0): 
        sum += n % 10
        n = n // 10
    return sum 
 
def reverse(n): 
    rev = 0
    while (n > 0): 
        dig = n % 10
        rev = (rev * 10) + dig 
        n = n // 10
    return rev 
 
def divisible_by_digit_sum(n): 
    rev = reverse(n) 
    if (n % digit_sum(n) == 0 and rev % digit_sum(rev) == 0): 
        return True
    return False
 
def find_numbers(n): 
    count = 0
    for i in range(1, n + 1): 
        if (divisible_by_digit_sum(i)): 
            count += 1
    return count 
 
if __name__ == '__main__': 
    n = int(input()) 
    print(find_numbers(n)) 
































































































































































































































