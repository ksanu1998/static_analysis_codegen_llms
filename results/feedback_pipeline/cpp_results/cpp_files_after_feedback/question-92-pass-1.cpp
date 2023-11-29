#include <bits/stdc++.h>
using namespace std;
void createSets(int N) {
    vector<int> nums(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }
    sort(nums.begin(), nums.end());
    int gcd = 1;
    for (int i = 0; i < N; i++) {
        gcd = __gcd(gcd, nums[i]);
    }
    if (gcd > 1) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
int main() {
    int N;
    cin >> N;
    createSets(N);
    return 0;
}