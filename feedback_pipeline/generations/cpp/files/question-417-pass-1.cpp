#include <stdio.h> 
int getTotalNumberOfSequences(int m, int n) {
    int count = 0;
    for (int i = m; i <= n; i++) {
        count++;
    }
    return count;
}