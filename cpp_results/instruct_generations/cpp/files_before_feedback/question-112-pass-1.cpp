#include <bits/stdc++.h> 
 using namespace std ;
long long int minOperations ( long long int A, long long int B ) {
    long long int diff = abs(A - B);
    long long int count = 0;
    while (diff > 0) {
        count++;
        diff--;
    }
    return count;
}