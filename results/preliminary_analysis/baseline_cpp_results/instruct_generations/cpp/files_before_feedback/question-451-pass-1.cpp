#include <bits/stdc++.h> 
 using namespace std ;
int countPalindromes(string S) {
    int n = S.length();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            string substring = S.substr(i, j - i + 1);
            if (isPalindrome(substring)) {
                count++;
            }
        }
    }
    return count;
}

bool isPalindrome(string s) {
    int n = s.length();
    for (int i = 0; i < n / 2; i++) {
        if (s[i]!= s[n - i - 1]) {
            return false;
        }
    }
    return true;
}