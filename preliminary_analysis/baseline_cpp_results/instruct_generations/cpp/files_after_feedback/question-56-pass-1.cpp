#include <iostream>
using namespace std;
float productOfGP(float a, float r, int n) {
    float product = 1;
    for (int i = 0; i < n; i++) {
        product *= (a * (1 - r));
        a *= r;
    }
    return product;
}
int main() {
    float a, r, n;
    cout << "Enter the first term, common ratio and number of terms: ";
    cin >> a >> r >> n;
    cout << "The product of the first " << n << " terms is " << productOfGP(a, r, n) << endl;
    return 0;
}