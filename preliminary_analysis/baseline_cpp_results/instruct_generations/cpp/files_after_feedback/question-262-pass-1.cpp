#include <bits/stdc++.h>
using namespace std;
string getNumber(const string& s) {
    string number;
    for (int i = 0; i < s.length(); i++) {
        if (isdigit(s[i])) {
            number += s[i];
        }
    }
    return number;
}
int main() {
    string s = "abc123";
    string number = getNumber(s);
    cout << number << endl;
    return 0;
}