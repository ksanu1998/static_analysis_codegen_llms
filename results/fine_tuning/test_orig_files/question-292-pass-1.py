MAX = 1000
arr = []


def ulam():

def ulam(max):
    arr = [1]
    for i in range(2, max + 1):
        if i % 2 == 0 or i % 3 == 0:
            continue
        arr.append(i)
    return arr
