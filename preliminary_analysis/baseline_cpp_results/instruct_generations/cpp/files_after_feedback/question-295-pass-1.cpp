#include <bits/stdc++.h>
using namespace std;
#define MAX 10000
vector<int> arr;
void ulam() {
    int i, j, k, count = 0;
    for (i = 2; i <= MAX; i++) {
        if (arr[i] == 0) {
            count++;
            for (j = i + i; j <= MAX; j += i) {
                arr[j] = 1;
            }
        }
    }
    cout << "Ulam Number Sequence : " << count << endl;
}