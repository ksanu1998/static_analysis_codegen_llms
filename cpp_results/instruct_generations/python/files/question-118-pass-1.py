import math


def insertPF(primeFact, fact):
    if fact in primeFact:
        return primeFact
    else:
        primeFact.append(fact)
        return primeFact