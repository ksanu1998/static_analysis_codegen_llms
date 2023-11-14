#include <bits/stdc++.h> 
 using namespace std ;
 pair < int , int > count_ht ( char s , int N ) {
 pair < int , int > p ;
 if ( s == ' H ' ) {
 p . first = floor ( N / 2.0 ) ;
 p . second = ceil ( N / 2.0 ) ;
 } else if ( s == ' T ' ) {
#include <bits/stdc++.h>
using namespace std;

pair<int, int> count_ht(char s, int N) {
    pair<int, int> p;
    if (s == 'H') {
        p.first = floor(N / 2.0);
        p.second = ceil(N / 2.0);
    } else if (s == 'T') {
        p.first = N - floor(N / 2.0);
        p.second = N - ceil(N / 2.0);
    }
    return p;
}