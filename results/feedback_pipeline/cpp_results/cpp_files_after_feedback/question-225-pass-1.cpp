#include <bits/stdc++.h>
using namespace std;
#define N 1000005
int primeFactors[N];
void findPrimeFactors() {
    // Initialize all prime factors as 1
    for (int i = 0; i < N; i++) {
        primeFactors[i] = 1;
    }
    // Find the prime factors of each number
    for (int i = 2; i < N; i++) {
        // If the number is not marked as prime, then it is not a prime factor
        if (primeFactors[i] == 0) {
            continue;
        }
        // Mark all its multiples as not prime
        for (int j = i * i; j < N; j += i) {
            primeFactors[j] = 0;
        }
    }
}