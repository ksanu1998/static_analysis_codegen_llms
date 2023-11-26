def isPossible(S, R, N):


'NEW_LINEINDENTcntl=0NEW_LINEcntr=0NEW_LINEDEDENT'
 cntu = 0
  cntd = 0
   for i in range(N):
        if (S[i] == 'L'):
            cntl += 1
        elif (S[i] == 'R'):
            cntr += 1
        elif (S[i] == 'U'):
            cntu += 1
        else:
            cntd += 1
    if (max (max (cntl , cntr ), max (cntu , cntd )) >= R ):
        return "Yes"
    mp = {}
    r_square = R * R
    i = 1
    while i * i <= r_square:
        mp[i * i] = i
        if ((r_square - i * i) in mp):
            if (max (cntl ,cntr ) >= mp [r_square - i * i ] and max (cntu ,cntd )>=i ):
                return "Yes"
            if (max (cntl ,cntr ) >= i and max (cntu ,cntd ) >= mp [r_square - i *i ]):
                return "Yes"
        i += 1
    return "No"
if __name__ == "__main__":
    S = "RDLLDDLDU"
    R = 5
    N = len(S)
    print (isPossible (S, R, N))
