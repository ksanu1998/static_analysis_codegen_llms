#include <bits/stdc++.h> 
 using namespace std ;
int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int count = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                count++;
            }
        }
        cout << count << " ";
    }
    return 0;
}