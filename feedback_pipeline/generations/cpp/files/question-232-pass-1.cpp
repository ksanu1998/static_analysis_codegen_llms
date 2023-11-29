#include <iostream> 
 using namespace std ;
int getMinNum(int a, int b, int c) {
    int minNum = 0;
    for (int i = a; i <= b; i++) {
        if (i % c == 0 && i > 0) {
            minNum = i;
            break;
        }
    }
    return minNum;
}