fact = [0] * 21



def preCompute():
    fact[0] = 1
    for i in range(1, 21):
        fact[i] = i * fact[i - 1]
