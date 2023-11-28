#include <bits/stdc++.h>
using namespace std;
bool divisorsSame(int n) {
    int countEvenDivisors = 0;
    int countOddDivisors = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            if (i % 2 == 0) {
                countEvenDivisors++;
            } else {
                countOddDivisors++;
            }
        }
    }
    return countEvenDivisors == countOddDivisors;
}