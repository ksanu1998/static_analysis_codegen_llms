#include <iostream>
using namespace std;
double sum(int x, int n) {
    double sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += pow(x, i) / factorial(i + 1);
    }
    return sum;
}