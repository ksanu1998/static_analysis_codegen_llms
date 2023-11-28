import sys


def steps(source, step, dest):
    if (abs(source) > (dest)):
        return sys .maxsize
    if (source == dest):
        return step
    pos = steps(source + step + 1, step + 1, dest)
    neg = steps(source - step - 1, step + 1, dest)
    return min(pos, neg)


dest = 11
print("No. of steps required", " to reach ", dest, " is ", steps(0, 0, dest))
