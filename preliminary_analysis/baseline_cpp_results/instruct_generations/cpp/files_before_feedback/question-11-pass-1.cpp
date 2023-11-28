#include <bits/stdc++.h> 
 using namespace std ;
 void count_setbit ( int N ) {
int count = 0;
while (N > 0) {
    N = N & (N - 1);
    count++;
}
cout << "The minimum number of coins required to obtain " << N << " is " << count << "." << endl;
}