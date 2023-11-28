def matchClosing(X, start, end, open, close):
    count = 0
    for i in range(start, end):
        if X[i] == open:
            count += 1
        elif X[i] == close:
            count -= 1
        if count < 0:
            return False
    return count == 0
