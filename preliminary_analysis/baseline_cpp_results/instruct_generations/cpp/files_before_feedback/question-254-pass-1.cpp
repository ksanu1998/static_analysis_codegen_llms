#include <bits/stdc++.h> 
 using namespace std ;
 void find ( int n ) {
int a, b;
for (a = 1; a <= n; a++) {
    for (b = 1; b <= n; b++) {
        if (a * a + b * b == n * n) {
            cout << "a = " << a << ", b = " << b << endl;
        }
    }
}