#include <bits/stdc++.h> 
 using namespace std ;
int countNumber(int N, int S) {
    int count = 0;
    for (int i = 1; i <= N; i++) {
        int sum = 0;
        for (int j = i; j <= N; j++) {
            sum += j;
            if (sum > S) {
                count++;
                break;
            }
        }
    }
    return count;
}