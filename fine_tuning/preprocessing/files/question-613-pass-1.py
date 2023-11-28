def makeAndCheckString(words, str):[PYTHON]
    def makeAndCheckString(words, str):
        for i in range(len(words)):
            if words[i] in str:
                continue
            else:
                return False
        return True
