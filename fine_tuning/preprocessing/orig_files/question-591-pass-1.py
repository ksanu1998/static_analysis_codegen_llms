def getMaxOccurringChar(str):
    freq = [0 for i in range(100)]
    max = -1
    len__ = len(str)


'NEW_LINEINDENTforiinrange(0,len__,1):NEW_LINEINDENTfreq[ord(str[i])-ord('a ')]+=1NEW_LINEDEDENTDEDENT'
   for i in range(26):
        if (max < freq[i]):
            max = freq[i]
            result = chr(ord('a') + i)
    return result
if __name__ == '__main__':
    str = "sample program"
    print ("Maximum occurring character =", getMaxOccurringChar (str))
