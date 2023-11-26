def smallestlexicographicstring(s, k):
    n = len(s)


'NEW_LINEINDENTif(k>=n):NEW_LINEINDENTforiinrange(n):NEW_LINEINDENTs[i]='a ';NEW_LINEDEDENTprint(s,end=' ')NEW_LINEreturn;NEW_LINEDEDENTforiinrange(n):NEW_LINEINDENTif(k==0):NEW_LINEINDENTbreak;NEW_LINEDEDENTif(s[i]=='a '):NEW_LINEINDENTcontinue;NEW_LINEDEDENTforjinrange(i+1,n):NEW_LINEINDENTif(s[j]>s[i]):NEW_LINEINDENTs[j]=s[i];NEW_LINEbreak;NEW_LINEDEDENTelif(j==n-1):NEW_LINEINDENTs[j]=s[i];NEW_LINEDEDENTDEDENTs[i]='a ';NEW_LINEk-=1NEW_LINEDEDENTprint(' '.join(s),end=' ');NEW_LINEDEDENTif__name__=='_ _ main _ _ ':
    s = list("geeksforgeeks")
    k = 6
    smallestlexicographicstring(s, k)
