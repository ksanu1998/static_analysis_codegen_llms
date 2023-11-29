#include <iostream> 
 using namespace std ;
int getMaxNum(int a, int b, int c) {
    int maxNum = 0;
    for (int i = a; i <= b; i++) {
        if (i % c == 0 && i > maxNum) {
            maxNum = i;
        }
    }
    return maxNum;
}