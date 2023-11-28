def isPalRec(st, s, e):
    if s >= e:
        return True
    if st[s]!= st[e]:
        return False
    return isPalRec(st, s+1, e-1)
