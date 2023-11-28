def markingScheme(N, answerKey, studentAnswer):

def markingScheme(N, answerKey, studentAnswer):
    totalMarks = 0
    for i in range(N):
        if answerKey[i] == studentAnswer[i]:
            totalMarks += 1
    return totalMarks
