def Validate(M):
    lenn = len(M)
    temp = ""
    for i in range(lenn):
        if (M[i].isdigit()):
            temp += M[i]
    nwlenn = len(temp)
    if (nwlenn != 10):
        print("Invalid")
        return
    res = ""
    x = temp[0:3]
    res += "(" + x + ")-"
    x = temp[3:3 + 3]
    res += "(" + x + ")-"
    x = temp[6:3 + 6]
    res += "(" + x + ")-"
    x = temp[9:1 + 9]
    res += "(" + x + ")"
    print(res)


if __name__ == '__main__':
    M = "91 234rt5%34*0 3"
    Validate(M)
