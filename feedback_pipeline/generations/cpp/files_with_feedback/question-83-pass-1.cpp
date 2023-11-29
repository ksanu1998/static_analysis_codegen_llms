#include <iostream>
int count_pairs(int x) {
    int count = 0;
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= x; j++) {
            if ((i & j) == x) {
                count++;
            }
        }
    }
    return count;
}