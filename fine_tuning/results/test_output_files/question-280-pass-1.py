def markingScheme(N, answerKey, studentAnswer):
    totalMarks = 0
    for i in range(N):
        if (answerKey[i] == studentAnswer[i]):
            totalMarks += 1
    print(totalMarks)


if __name__ == "__main__":
    N = 3
    answerKey = [1, 2, 3]
    studentAnswer = [1, 2, 3]
    markingScheme(N, answerKey, studentAnswer)
