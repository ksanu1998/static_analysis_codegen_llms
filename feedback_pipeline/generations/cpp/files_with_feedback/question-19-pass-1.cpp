#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
void findMode(int a[], int n) {
    // Create a vector to store the elements of the array
    vector<int> v(a, a + n);
    // Find the mode using the any_of, all_of, and none_of algorithms
    auto mode = find_if(v.begin(), v.end(), [&](int x) {
        return any_of(v.begin(), v.end(), [&](int y) { return y == x; });
    });
    // Print the mode
    cout << "Mode: " << *mode << endl;
}
int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(a) / sizeof(a[0]);
    findMode(a, n);
    return 0;
}