#include <bits/stdc++.h> 
 using namespace std ;
long long numbers(int n) {
    long long count = 0;
    for (int i = 3; i <= 4; i++) {
        for (int j = i; j <= n; j++) {
            count++;
        }
    }
    return count;
}