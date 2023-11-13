#include <bits/stdc++.h> 
 using namespace std ;
 void solve ( string s ) {
#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int i = s.find('+');
    if (i == -1) {
        cout << "No conjugate found." << endl;
        return 0;
    }
    string real = s.substr(0, i);
    string imag = s.substr(i + 1);
    if (imag[0] == '-') {
        imag = imag.substr(1);
    } else {
        imag = '-' + imag;
    }
    cout << real << "+" << imag << "i" << endl;
    return 0;
}