#include <bits/stdc++.h> 
 using namespace std ;
static long sumOfSumSeries(int N) {
    long sum = 0;
    for (int i = 1; i <= N; i++) {
        sum += i;
    }
    return sum;
}