from math import pow
'NEW_LINEdefno_of_characters(M):NEW_LINEINDENTk=1NEW_LINEwhile(True):NEW_LINEINDENTif(pow(2,k+1)-2<M):NEW_LINEINDENTk+=1NEW_LINEDEDENTelse:NEW_LINEINDENTbreakNEW_LINEDEDENTDEDENTreturnkNEW_LINEDEDENT'


def print_string(M):
    k = no_of_characters(M)
    N = M - (pow(2, k) - 2)
    while (k > 0):
        num = pow(2, k - 1)
        if (num >= N):
            print("A", end="")
        else:
            print("B", end="")
            N -= num
        k -= 1
    print("",  end  = "")


if __name__ == '__main__':
    M = 30
    print_string(M)
    M = 55
    print_string(M)
    M = 100
    print_string(M)
