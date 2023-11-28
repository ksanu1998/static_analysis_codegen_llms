#include <iostream>
int countStaircases(int N) {
    int count = 0;
    for (int i = 1; i <= N; i++) {
        count += i;
    }
    return count;
}