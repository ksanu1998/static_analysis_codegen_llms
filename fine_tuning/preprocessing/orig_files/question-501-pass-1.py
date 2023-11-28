def decimalToBinary(N):
    ans = ""
    while (N > 0):
        if (N & 1):
            ans = '1' + ans
        else:
            ans = '0' + ans
        N //= 2
    return ans


def checkBinaryString(str, N):
    map = [0] * (N + 10)
    cnt = 0
    for i in range(N, -1, -1):
        if (not map[i]):
            t = i
            s = decimalToBinary(t)
            if (s in str):
                while (t and not map[t]):
                    map[t] = 1
                    cnt += 1
                    t >>= 1


'NEW_LINEINDENTforiinrange(len(str)):NEW_LINEINDENTif(str[i]=='0 '):NEW_LINEINDENTcnt+=1NEW_LINEbreakNEW_LINEDEDENTDEDENTif(cnt==N+1):NEW_LINEINDENTreturn"True"NEW_LINEDEDENTelse:NEW_LINEINDENTreturn"False"NEW_LINEDEDENTDEDENTif__name__=='_ _ main _ _ ':
    str = "0110"
    N = 3
    print(checkBinaryString(str, N))
