#include <bits/stdc++.h> 
 using namespace std ;
int Triplets(int n) {
    int count = 0;
    for (int a = 1; a <= n; a++) {
        for (int b = a; b <= n; b++) {
            int c = sqrt(a * a + b * b);
            if (c * c == a * a + b * b && 1 <= c && c <= n) {
                count++;
            }
        }
    }
    return count;
}