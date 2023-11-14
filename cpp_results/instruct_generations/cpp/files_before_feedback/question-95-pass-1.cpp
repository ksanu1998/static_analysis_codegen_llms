#include <bits/stdc++.h> 
 using namespace std ;
int findNthNumber(int N) {
    int n = 1;
    while (N > 0) {
        int digit = n % 10;
        int nextDigit = (n / 10) % 10;
        if (abs(digit - nextDigit) <= 1) {
            N--;
        }
        n++;
    }
    return n - 1;
}