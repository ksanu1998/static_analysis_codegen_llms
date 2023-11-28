#include <iostream> 
 #include <math.h> 
 using namespace std ;
int smallestNumber(int N) {
    int i = 1;
    while (i % N!= 0) {
        i++;
    }
    return i;
}