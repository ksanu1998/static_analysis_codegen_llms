#include <bits/stdc++.h> 
 using namespace std ;
bool isTetradecagonal(int N) {
    int sum = 0;
    for (int i = 1; i <= N; i++) {
        sum += i * i * i;
    }
    return sum == N;
}