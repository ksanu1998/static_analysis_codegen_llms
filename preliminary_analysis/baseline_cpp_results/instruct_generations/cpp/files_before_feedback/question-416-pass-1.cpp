#include <iostream> 
 using namespace std ;
int getTotalNumberOfSequences(int m, int n) {
    int total = 1;
    for (int i = m; i <= n; i++) {
        total *= i;
    }
    return total;
}