#include <bits/stdc++.h>
using namespace std;
double find_probability(double p, double q, double r, double s) {
    return p * r / (p * r + q * s);
}
int main() {
    double p, q, r, s;
    cin >> p >> q >> r >> s;
    double probability = find_probability(p, q, r, s);
    cout << "Probability: " << probability << endl;
    return 0;
}