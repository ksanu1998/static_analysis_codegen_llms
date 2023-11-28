#include <bits/stdc++.h> 
 using namespace std ;
int countOrderedPairs(int N) {
    int count = 0;
    for (int i = 1; i < N; i++) {
        for (int j = i + 1; j <= N; j++) {
            count++;
        }
    }
    return count;
}