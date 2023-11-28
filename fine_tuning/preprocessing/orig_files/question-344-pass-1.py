import numpy as np


def MaximumMarks(marksarr, timearr, h, n, p):
    no_of_topics = n + 1
    total_time = h + 1
    T = np .zeros((no_of_topics, total_time))
    for i in range(no_of_topics):
        T[i][0] = 0
    for j in range(total_time):
        T[0][j] = 0
    for i in range(1, no_of_topics):
        for j in range(1, total_time):
            if (j < timearr[i]):
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(marksarr[i] + T[i - 1]
                              [j - timearr[i]], T[i - 1][j])
    i = no_of_topics - 1
    j = total_time - 1
    sum = 0
    while (i > 0 and j > 0):
        if (T[i][j] == T[i - 1][j]):
            i -= 1
        else:
            sum += timearr[i]
            j -= timearr[i]
            i -= 1
    marks = T[no_of_topics - 1][total_time - 1]
    if (marks < p):
        return -1
    return sum


if __name__ == "__main__":
    n = 4
    h = 10
    p = 10
    marksarr = [0, 6, 4, 2, 8]
    timearr = [0, 4, 6, 2, 7]
    print(MaximumMarks(marksarr, timearr, h, n, p))
