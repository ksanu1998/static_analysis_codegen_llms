def countRepeatingDigits(N):

def countRepeatingDigits(N):
    count = 0
    for i in range(1, len(str(N))):
        if str(N)[:i] == str(N)[i:]:
            count += 1
    return count
