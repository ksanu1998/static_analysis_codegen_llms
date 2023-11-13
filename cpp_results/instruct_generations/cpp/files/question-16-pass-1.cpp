#include <bits/stdc++.h> 
 using namespace std ;
int alternatingSumOfFirst_N(int N) {
    int sum = 0;
    for (int i = 1; i <= N; i++) {
        sum += (i % 2 == 0)? i : -i;
    }
    return sum;
}