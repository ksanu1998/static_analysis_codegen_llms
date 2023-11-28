#include <bits/stdc++.h>
using namespace std;
pair<double, double> findingValues(double m, double n, double mth, double nth) {
    double d = (abs(mth - nth)) / abs((m - 1) - (n - 1));
    double a = mth - ((m - 1) * d);
    return make_pair(a, d);
}
double findSum(int m, int n, int mth, int nth, int p) {
    pair<double, double> values = findingValues(m, n, mth, nth);
    double a = values.first;
    double d = values.second;
    double sum = 0;
    for (int i = 1; i <= p; i++) {
        sum += a + (i - 1) * d;
    }
    return sum;
}