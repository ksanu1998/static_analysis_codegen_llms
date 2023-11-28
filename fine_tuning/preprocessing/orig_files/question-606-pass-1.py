def finalPosition(move):
    l = len(move)
    countUp, countDown = 0, 0
    countLeft, countRight = 0, 0


'NEW_LINEINDENTforiinrange(l):NEW_LINEINDENTif(move[i]=='U '):NEW_LINEINDENTcountUp+=1NEW_LINEDEDENTelif(move[i]=='D '):NEW_LINEINDENTcountDown+=1NEW_LINEDEDENTelif(move[i]=='L '):NEW_LINEINDENTcountLeft+=1NEW_LINEDEDENTelif(move[i]=='R '):NEW_LINEINDENTcountRight+=1NEW_LINEDEDENTDEDENTprint("Final Position: (",(countRight-countLeft),", ",(countUp-countDown),")")NEW_LINEDEDENTif__name__=='_ _ main _ _ ':
    move = "UDDLLRUUUDUURUDDUULLDRRRR"
    finalPosition(move)
