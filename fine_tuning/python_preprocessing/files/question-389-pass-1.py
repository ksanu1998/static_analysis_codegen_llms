N = 1000


def arrangeBraces(n, pos, k):
    if n == 0:
        return True
    if k == 0:
        return False
    if pos == n:
        return False
    if arr[pos] == '(':
        return arrangeBraces(n-1, pos+1, k) or arrangeBraces(n, pos+1, k-1)
    else:
        return arrangeBraces(n-1, pos+1, k)
