#include <bits/stdc++.h> 
 using namespace std ;
int check(int A, int B) {
    return (B * 10 + B % 10) % 10 == (A % 10);
}