#include <bits/stdc++.h> 
 using namespace std ;
int checkSame(int n, int b) {
    int count = 0;
    while (n > 0) {
        if (n % 10 == b) {
            count++;
        }
        n /= 10;
    }
    return count;
}