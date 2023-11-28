#include <bits/stdc++.h>
using namespace std;
double SumofInverseDivisors(int N, int Sum) {
    double sum = 0;
    for (int i = 1; i <= N; i++) {
        if (Sum % i == 0) {
            sum += 1.0 / i;
        }
    }
    return sum;
}