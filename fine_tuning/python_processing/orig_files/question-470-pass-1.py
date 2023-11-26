def findIfPossible(N, str_):
    countG = 0
    countF = 0
    for i in range(N):
        if str_[i] == 'G':
            countG += 1
        else:
            countF += 1
    if 2 * countF != countG:
        print("NO")
    else:
        id = 0
        flag = True
        for i in range(N):
            if str_[i] == 'G':
                countG -= 1
                id += 1
            else:
                countF -= 1
                id -= 1
            if id < 0:
                flag = False
                break
            if countG < countF:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")


n = 6
str_ = "GFGFGG"
findIfPossible(n, str_)
