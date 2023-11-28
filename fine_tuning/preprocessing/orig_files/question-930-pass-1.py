def sackRace(p1, s1, p2, s2):
    return ((s1 > s2 and (p2 - p1) %
             (s1 - s2) == 0) or (s2 > s1 and (p1 - p2) %
                                 (s2 - s1) == 0))


p1 = 4
s1 = 4
p2 = 8
s2 = 2
if (sackRace(p1, s1, p2, s2)):
    print("Yes")
else:
    print("No")
