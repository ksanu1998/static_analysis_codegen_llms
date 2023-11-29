#include <bits/stdc++.h> 
 using namespace std ;
 void solve ( int n ) {
int a, b;
for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
        if (pow(i - j, 4) == n) {
            a = i;
            b = j;
            break;
        }
    }
    if (a!= 0 && b!= 0) {
        break;
    }
}
cout << a << " " << b << endl;