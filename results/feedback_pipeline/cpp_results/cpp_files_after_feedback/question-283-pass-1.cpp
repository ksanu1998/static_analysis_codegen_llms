#include <bits/stdc++.h>
using namespace std;
int markingScheme(int N, int answerKey[], int studentAnswer[]) {
    int totalMarks = 0;
    for (int i = 0; i < N; i++) {
        if (answerKey[i] == studentAnswer[i]) {
            totalMarks += 10;
        } else if (answerKey[i]!= studentAnswer[i]) {
            totalMarks += 5;
        }
    }
    return totalMarks;
}