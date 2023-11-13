#include <bits/stdc++.h> 
 using namespace std ;
bool isPossible(int A, int B) {
    int prime = 2;
    while (prime <= A) {
        if (A % prime == 0 && B % prime == 0) {
            return true;
        }
        prime++;
    }
    return false;
}