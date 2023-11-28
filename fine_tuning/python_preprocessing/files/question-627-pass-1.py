def amend_sentence(string):
    words = string.split()
    for i in range(len(words)):
        if words[i].istitle():
            words[i] = words[i].lower()
    return " ".join(words)
