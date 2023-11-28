#include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long int 
ll findNumber(int n) {
    ll num = 1;
    for (int i = 2; i <= n; i++) {
        num = num * 10 + i;
    }
    return num;
}