#include <iostream> 
 using namespace std ;
 string X , Y ;
int lcs(int i, int j, int count) {
    if (i == 0 || j == 0) {
        return count;
    }
    if (X[i - 1] == Y[j - 1]) {
        return lcs(i - 1, j - 1, count + 1);
    } else {
        int a = lcs(i - 1, j, count);
        int b = lcs(i, j - 1, count);
        return a > b? a : b;
    }
}