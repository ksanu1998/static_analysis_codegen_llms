#include <iostream>
using namespace std;
int findX(int A, int B) {
    int x = 0;
    while (A!= B) {
        if (A < B) {
            B -= x;
        } else {
            A -= x;
        }
        x++;
    }
    return x;
}
int main() {
    int A, B;
    cin >> A >> B;
    cout << findX(A, B) << endl;
    return 0;
}