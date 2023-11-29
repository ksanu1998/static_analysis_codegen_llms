#include <bits/stdc++.h>
using namespace std;
int movesRequired(int a, int b) {
    int result = 0;
    while (a % b!= 0) {
        a--;
        result++;
    }
    return result;
}