#include <iostream>
using namespace std;
int count(const string& a, const string& b) {
    int count = 0;
    for (int i = 0; i < a.length(); i++) {
        if (a.substr(i, b.length()) == b) {
            count++;
        }
    }
    return count;
}
int main() {
    string a = "banana";
    string b = "ana";
    cout << count(a, b) << endl;
    return 0;
}