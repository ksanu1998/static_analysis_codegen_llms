from math import pow
'NEW_LINEdefno_of_characters(M):NEW_LINEINDENTk=1NEW_LINEwhile(True):NEW_LINEINDENTif(pow(2,k+1)-2<M):NEW_LINEINDENTk+=1NEW_LINEDEDENTelse:NEW_LINEINDENTbreakNEW_LINEDEDENTDEDENTreturnkNEW_LINEDEDENT'


def print_string(M):
    k = 1
    while True:
        if pow(2, k + 1) - 2 < M:
            k += 1
        else:
            break
    return k
