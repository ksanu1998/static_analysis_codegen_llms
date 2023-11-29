m = {}



def precompute():
    for i in range(1, 1000):
        m[i] = i * m.get(i - 1, 1)
