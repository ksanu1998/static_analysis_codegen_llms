#include <bits/stdc++.h> 
 using namespace std ;
long long findNthNumber(long long N) {
    long long count = 1;
    while (N > 0) {
        N--;
        count = count * 10;
    }
    return count;
}