#include <bits/stdc++.h>
using namespace std;
bool areAnagrams(int a, int b) {
    // Convert the integers to strings
    string str1 = to_string(a);
    string str2 = to_string(b);
    // Sort the strings
    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());
    // Check if the sorted strings are equal
    return str1 == str2;
}