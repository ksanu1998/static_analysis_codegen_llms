#include <bits/stdc++.h> 
 using namespace std ;
float sum(float n) {
    float sum = 0;
    for (float i = 1; i <= n; i++) {
        sum += 1/i;
    }
    return sum;
}