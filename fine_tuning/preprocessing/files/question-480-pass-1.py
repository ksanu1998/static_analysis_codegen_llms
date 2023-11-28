def addASCII(S, N):
    return ''.join(chr(ord(c) + N) for c in S)
