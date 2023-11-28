#include <cmath>
#include <iostream>
using namespace std;
int minimumLectures(int m, int n) {
    return ceil(m * 0.75) - n;
}
int main() {
    int m, n;
    cin >> m >> n;
    cout << minimumLectures(m, n) << endl;
    return 0;
}