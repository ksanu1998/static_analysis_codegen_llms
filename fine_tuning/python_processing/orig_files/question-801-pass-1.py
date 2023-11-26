def reverserWords(string):
    st = list()
    for i in range(len(string)):
        if string[i] != " ":
            st .append(string[i])
        else:
            while len(st) > 0:
                print(st[-1], end="")
                st .pop()
            print(end=" ")
    while len(st) > 0:
        print(st[-1], end="")
        st .pop()


if __name__ == "__main__":
    string = "Geeks for Geeks"
    reverserWords(string)
