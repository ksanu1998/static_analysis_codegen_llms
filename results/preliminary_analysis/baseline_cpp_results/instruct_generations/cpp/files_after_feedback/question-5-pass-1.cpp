#include <bits/stdc++.h>
using namespace std;
int countQuadruples(const array<int, 4>& nums) {
    int count = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            for (int k = j + 1; k < 4; k++) {
                for (int l = k + 1; l < 4; l++) {
                    if (nums[i] * nums[j] == nums[k] * nums[l]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
int main() {
    array<int, 4> nums = {1, 2, 3, 4};
    cout << countQuadruples(nums) << endl;
    return 0;
}