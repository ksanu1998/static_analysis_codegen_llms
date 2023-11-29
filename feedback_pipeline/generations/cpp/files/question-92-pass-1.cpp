#include <bits/stdc++.h> 
 using namespace std ;
int main() {
    int N;
    cin >> N;
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
    return 0;
}