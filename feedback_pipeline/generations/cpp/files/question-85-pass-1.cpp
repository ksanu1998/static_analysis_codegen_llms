#include <bits/stdc++.h> 
 using namespace std ;
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

void printPair(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            if (gcd(i, j) == n && lcm(i, j) == n) {
                cout << i << " " << j << endl;
                return;
            }
        }
    }
}