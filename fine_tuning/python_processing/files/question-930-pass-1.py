def sackRace(p1, s1, p2, s2):
    if p1 == p2 and s1 == s2:
        return True
    elif p1 > p2 and s1 > s2:
        return sackRace(p1 - p2, s1, p2, s2)
    elif p1 < p2 and s1 < s2:
        return sackRace(p1, s1, p2 - p1, s2)
    else:
        return False
