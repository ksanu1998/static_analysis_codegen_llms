#include <iostream>
#include <vector>
using namespace std;
void printDiagonalTraversal(vector<vector<int>> &nums) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < nums[i].size(); j++) {
            if (i == j) {
                cout << nums[i][j] << " ";
            }
        }
    }
    cout << endl;
}
int main() {
    vector<vector<int>> nums = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    printDiagonalTraversal(nums);
    return 0;
}