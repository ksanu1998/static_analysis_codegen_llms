def markingScheme(N, answerKey, studentAnswer):
    totalMarks = 0
    for i in range(N):
        if answerKey[i] == studentAnswer[i]:
            totalMarks += 4
        else:
            totalMarks += 0
    return totalMarks
