#include <bits/stdc++.h> 
 using namespace std ;
 void updateMatrix ( int n , int q [ 3 ] [ 4 ] ) {
for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (q[i][j] == 1) {
                q[i][j] = 0;
            } else {
                q[i][j] = 1;
            }
        }
    }
}