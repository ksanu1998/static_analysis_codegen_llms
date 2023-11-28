import sys


def steps(source, step, dest):
    if source == dest:
        return 0
    elif source + step == dest or source - step == dest:
        return 1
    else:
        return 2
