#include <bits/stdc++.h> 
 using namespace std ;
string getNumber(string s) {
    string number;
    for (int i = 0; i < s.length(); i++) {
        if (isdigit(s[i])) {
            number += s[i];
        }
    }
    return number;
}