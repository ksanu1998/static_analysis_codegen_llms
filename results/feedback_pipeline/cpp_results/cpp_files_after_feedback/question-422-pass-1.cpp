#include <iostream>
using namespace std;
const int templeHeight[] = {1, 2, 3, 4, 5};
int offeringNumber(int n, const int templeHeight[]) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (templeHeight[i] > 0) {
            count++;
        }
    }
    return count;
}
int main() {
    int n;
    cin >> n;
    int templeHeight[n];
    for (int i = 0; i < n; i++) {
        cin >> templeHeight[i];
    }
    int count = offeringNumber(n, templeHeight);
    cout << count << endl;
    return 0;
}