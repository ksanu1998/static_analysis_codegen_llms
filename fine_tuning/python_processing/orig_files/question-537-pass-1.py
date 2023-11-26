def minLength(string, l):
    s = []
    for i in range(l):
        if (len(s) == 0):
            s .append(string[i])
        else:
            c = s[-1]
            if (c != string[i] and c .upper() == string[i].upper()):
                s .pop()
            else:
                s .append(string[i])
    return len(s)


if __name__ == "__main__":
    string = "ASbBsd"
    l = len(string)
    print(minLength(string, l))
