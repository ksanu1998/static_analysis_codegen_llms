#include <bits/stdc++.h> 
 using namespace std ;
int NoofTriplets(int N, int K) {
    int count = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = i + 1; j <= N; j++) {
            for (int k = j + 1; k <= N; k++) {
                if (i + j + k <= N && i * j * k % K == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}