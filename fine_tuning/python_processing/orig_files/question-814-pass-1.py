def findDuplicateparenthesis(string):
    Stack = []
    for ch in string:
        if ch == ')':
            top = Stack .pop()
            elementsInside = 0
            while top != '(':
                elementsInside += 1
                top = Stack .pop()
            if elementsInside < 1:
                return True
        else:
            Stack .append(ch)
    return False


if __name__ == "__main__":
    string = "(((a+(b))+(c+d)))"
    if findDuplicateparenthesis(string):
        print("Duplicate Found")
    else:
        print("No Duplicates Found")
