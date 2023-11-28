#include <bits/stdc++.h> 
 using namespace std ;
int NumberOfRectangles(int n, int m) {
    int count = 0;
    for (int i = 0; i <= n - 2; i++) {
        for (int j = 0; j <= m - 1; j++) {
            if (i + 2 <= n && j + 1 <= m) {
                count++;
            }
        }
    }
    return count;
}