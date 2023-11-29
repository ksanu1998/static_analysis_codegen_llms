def countSetBits(n):

def countSetBits(n):
    count = 0
    for i in range(1, n+1):
        binary = bin(i)
        count += binary.count('1')
    return count
