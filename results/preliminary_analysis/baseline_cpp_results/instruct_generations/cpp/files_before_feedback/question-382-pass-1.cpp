#include <bits/stdc++.h> 
 using namespace std ;
 int term [ 1000 ] ;
 int fib ( int n ) {
int term[1000];
int fib(int n) {
    if (n <= 1) {
        return n;
    }
    if (term[n]!= 0) {
        return term[n];
    }
    term[n] = fib(n - 1) + fib(n - 2);
    return term[n];
}