#include <bits/stdc++.h> 
 using namespace std ;
 void solve ( int n ) {
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;
    for (int i = 1; i <= n; i++) {
        int num = i;
        int rev = 0;
        while (num!= 0) {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        if (rev == i) {
            count++;
        }
    }
    cout << count << "\n";
    return 0;
}