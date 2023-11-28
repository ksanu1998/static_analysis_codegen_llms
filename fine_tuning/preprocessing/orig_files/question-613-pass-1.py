def makeAndCheckString(words, str):
    n = len(words)
    first = second = False
    for i in range(n):
        if words[i] == str:
            return True
        if str[0] == words[i][1]:
            first = True
        if str[1] == words[i][0]:
            second = True
        if first and second:
            return True
    return False


str = 'ya'
words = ['ah', 'oy', 'to', 'ha']
if makeAndCheckString(words, str):
    print('YES')
else:
    print('NO')
