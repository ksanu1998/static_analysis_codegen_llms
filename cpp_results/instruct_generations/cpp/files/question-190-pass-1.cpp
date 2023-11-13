#include <iostream> 
 using namespace std ;
bool isSumEqual(int ar[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += ar[i];
    }
    return sum == n;
}