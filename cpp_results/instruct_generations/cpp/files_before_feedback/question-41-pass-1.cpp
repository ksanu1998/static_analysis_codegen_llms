#include <iostream> 
 #include <math.h> 
 using namespace std ;
long sumOfSumSeries(int n) {
    long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i * (i + 1) / 2;
    }
    return sum;
}