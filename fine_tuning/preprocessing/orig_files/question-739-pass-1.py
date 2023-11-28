def predictTheWinner(K, N):
    if (N % (K + 1) == 0):
        print("Bob")
    else:
        print("Alice")


if __name__ == '__main__':
    K = 7
    N = 50
    predictTheWinner(K, N)
