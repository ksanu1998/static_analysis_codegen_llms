#include <bits/stdc++.h> 
 using namespace std ;
double find_probability(double p, double q, double r, double s) {
    return p * r / (p * r + q * s);
}