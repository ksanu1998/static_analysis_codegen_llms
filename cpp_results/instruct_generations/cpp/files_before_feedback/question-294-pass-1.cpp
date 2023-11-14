#include <cmath> 
 #include <iostream> 
 using namespace std ;
int numberOfDistinct(int n) {
    return (int)std::lcm(n, n);
}