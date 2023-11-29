#include <iostream> 
 using namespace std ;
int countSetBits(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        count += __builtin_popcount(i);
    }
    return count;
}