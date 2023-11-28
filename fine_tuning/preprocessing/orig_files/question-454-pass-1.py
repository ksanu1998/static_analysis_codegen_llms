import math


def count_ht(s, N):
    if s == "H":
        h = math .floor(N / 2)
        t = math .ceil(N / 2)
    elif s == "T":
        h = math .ceil(N / 2)
        t = math .floor(N / 2)
    return [h, t]


if __name__ == "__main__":
    C = "H"
    N = 5
    l = count_ht(C, n)
    print("Head = ", l[0])
    print("Tail = ", l[1])
