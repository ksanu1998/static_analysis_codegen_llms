#include <iostream>
using namespace std;
string checkNumber(int N) {
    string result;
    if (N == 144) {
        result = "144";
    } else if (N == 14) {
        result = "14";
    } else if (N == 1) {
        result = "1";
    } else {
        result = "Invalid";
    }
    return result;
}
int main() {
    int N;
    cin >> N;
    cout << checkNumber(N) << endl;
    return 0;
}