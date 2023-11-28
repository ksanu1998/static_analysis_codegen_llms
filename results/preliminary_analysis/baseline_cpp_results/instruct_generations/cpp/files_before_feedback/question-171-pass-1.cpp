#include <iostream> 
 using namespace std ;
 int sum ( int A , int B , int R ) {
int sum = 0;
for (int i = 0; i < R; i++) {
    sum += A[i] + B[i];
}
return sum;