#include <bits/stdc++.h> 
 using namespace std ;
int count_pairs(int a[], int b[], int N) {
    int count = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (a[i] + a[j] > b[i] + b[j]) {
                count++;
            }
        }
    }
    return count;
}