#include <iostream>
using namespace std;
int findLength(const string& str, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (str[i] == '0') {
            count++;
        }
    }
    return count;
}
int main() {
    string str;
    cin >> str;
    int n = str.length();
    int count = findLength(str, n);
    cout << count << endl;
    return 0;
}