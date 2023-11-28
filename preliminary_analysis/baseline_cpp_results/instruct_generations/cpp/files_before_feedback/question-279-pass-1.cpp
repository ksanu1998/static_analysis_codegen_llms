#include <bits/stdc++.h> 
 using namespace std ;
int countNumbers(int N) {
    int count = 0;
    for (int i = 1; i <= N; i++) {
        int root = (int)sqrt(i);
        if (root * root == i) {
            count++;
        }
    }
    return count;
}