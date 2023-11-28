import random
import math
e = 2.71828


def roundNo(num):
    if (num < 0):
        return (num - 0.5)
    else:
        return (num + 0.5)


def printBestCandidate(candidate, n):
    sample_size = roundNo(n / e)
    print("Samplesizeis", math .floor(sample_size))
    best = 0
    for i in range(1, int(sample_size)):
        if (candidate[i] > candidate[best]):
            best = i
    for i in range(int(sample_size), n):
        if (candidate[i] >= candidate[best]):
            best = i
            break
    if (best >= int(sample_size)):
        print(
            "Bestcandidatefoundis",
            math .floor(
                best + 1),
            "with talent",
            math .floor(
                candidate[best]))
    else:
        print("Couldn't find a best candidate")


n = 8
candidate = [0] * (n)
for i in range(n):
    candidate[i] = 1 + random .randint(1, 8)
print("Candidate : ", end="")
for i in range(n):
    print((i + 1), end=" ")
print("Talents:",  end  = "")
for i in range(n):
    print(candidate[i], end=" ")
printBestCandidate(candidate, n)
