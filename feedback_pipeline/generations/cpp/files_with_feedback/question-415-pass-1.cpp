#include <iostream>
#include <vector>
using namespace std;
int countWays(const vector<int>& arr, int m, int N) {
    int dp[N+1];
    dp[0] = 1;
    for(int i=1; i<=N; i++) {
        for(int j=0; j<m; j++) {
            if(arr[j] <= i) {
                dp[i] += dp[i-arr[j]];
            }
        }
    }
    return dp[N];
}
int main() {
    int m, N;
    cin >> m >> N;
    vector<int> arr(m);
    for(int i=0; i<m; i++) {
        cin >> arr[i];
    }
    cout << countWays(arr, m, N) << endl;
    return 0;
}