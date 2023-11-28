#include " bits / stdc + + . h " 
 #define ll  long long int 
 using namespace std ;
 map < ll , ll > m ;
int precompute() {
    m[0] = 1;
    m[1] = 1;
    for (ll i = 2; i <= 1000000; i++) {
        m[i] = m[i - 1] + m[i - 2];
    }
    return 0;
}