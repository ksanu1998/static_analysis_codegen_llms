#include <iostream>
#include <string>
using namespace std;
const int MAX = 40;
int dp[MAX][9 * MAX + 1];
int countGroups(int position, int previous_sum, int length, char* num) {
    if (position == length) {
        return 1;
    }
    if (dp[position][previous_sum]!= -1) {
        return dp[position][previous_sum];
    }
    int count = 0;
    for (int i = 0; i < 9; i++) {
        if (previous_sum + i * pow(10, length - position - 1) <= MAX) {
            count += countGroups(position + 1, previous_sum + i * pow(10, length - position - 1), length, num);
        }
    }
    return dp[position][previous_sum] = count;
}
int main() {
    int length;
    cin >> length;
    char num[length + 1];
    cin >> num;
    int previous_sum = 0;
    for (int i = 0; i < length; i++) {
        previous_sum = previous_sum * 10 + (num[i] - '0');
    }
    cout << countGroups(0, previous_sum, length, num) << endl;
    return 0;
}