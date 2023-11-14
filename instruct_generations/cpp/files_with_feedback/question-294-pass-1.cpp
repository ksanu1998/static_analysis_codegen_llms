#include <cmath>
#include <iostream>
using namespace std;
int numberOfDistinct(int n) {
    return (int)std::lcm(n, n);
}
int main() {
    int n;
    cin >> n;
    cout << numberOfDistinct(n) << endl;
    return 0;
}