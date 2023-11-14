#include <bits/stdc++.h> 
 using namespace std ;
int minSwaps(vector<vector<int>>& b) {
    int n = b.size();
    int m = b[0].size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m - 1; j++) {
            if (b[i][j] == b[i][j + 1]) {
                count++;
                int temp = b[i][j];
                b[i][j] = b[i][j + 1];
                b[i][j + 1] = temp;
            }
        }
    }
    return count;
}