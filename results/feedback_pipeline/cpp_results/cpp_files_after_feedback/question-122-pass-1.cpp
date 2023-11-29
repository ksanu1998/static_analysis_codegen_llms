#include <iostream>
#include <map>
using namespace std;
int main() {
    int n;
    cin >> n;
    cout << n << "! = " << factorial(n) << endl;
    return 0;
}
int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}