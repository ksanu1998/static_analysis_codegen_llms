def printSubsInDelimeters(string):
    dels = []
    for i in range(len(string)):
        if (string[i] == '['):
            dels .append(i)
        elif (string[i] == ']' and len(dels) != 0):
            pos = dels[-1]
            dels .pop()
            length = i - 1 - pos
            ans = string[pos + 1:pos + 1 + length]
            print(ans)


if __name__ == "__main__":
    string = "[This is first] ignored text [This is second]"
    printSubsInDelimeters(string)
