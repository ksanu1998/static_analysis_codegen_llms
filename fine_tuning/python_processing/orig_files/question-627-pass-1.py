def amendSentence(string):
    string = list(string)
    for i in range(len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            string[i] = chr(ord(string[i]) + 32)
            if i != 0:
                print(" ", end="")
            print(string[i], end="")
        else:
            print(string[i], end="")


if __name__ == "__main__":
    string = "BruceWayneIsBatman"
    amendSentence(string)
