#include <bits/stdc++.h> 
 using namespace std ;
int chordCnt(int A) {
    int count = 0;
    for (int i = 1; i <= A; i++) {
        count += i;
    }
    return count;
}