from math import sqrt


def findValuesOfK(g):
    count = 0
    for i in range(1, int(sqrt(g)) + 1, 1):
        if (g % i == 0):
            if (i != g // i):
                if (i & 1):
                    count += 1
                if ((g // i) & 1):
                    count += 1
            elif (i & 1):
                count += 1
    print(count)


if __name__ == '__main__':
    G = 125
    findValuesOfK(G)
