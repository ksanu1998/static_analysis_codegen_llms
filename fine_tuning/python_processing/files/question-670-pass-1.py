def checkReachability(N, X, Y):
    if N == 0:
        return False
    if X == 0 and Y == 0:
        return True
    if X > 0 and Y > 0:
        return checkReachability(N-1, X-1, Y) or checkReachability(N-1, X, Y-1)
    elif X < 0 and Y < 0:
        return checkReachability(N-1, X+1, Y) or checkReachability(N-1, X, Y+1)
    else:
        return checkReachability(N-1, X+1, Y) or checkReachability(N-1, X, Y+1) or checkReachability(N-1, X-1, Y) or checkReachability(N-1, X, Y-1)
