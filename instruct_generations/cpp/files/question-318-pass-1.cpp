#include <bits/stdc++.h> 
 using namespace std ;
int numberOfArithmeticSequences(int L[], int N) {
    int count = 0;
    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                if (L[k] - L[j] == L[j] - L[i]) {
                    count++;
                }
            }
        }
    }
    return count;
}