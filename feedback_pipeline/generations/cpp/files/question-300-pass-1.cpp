#include <bits/stdc++.h> 
 using namespace std ;
double sumProductDifference(int a, int b, int c, int d, int e) {
    // Calculate the roots of the quartic equation
    double root1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a);
    double root2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a);
    double root3 = (-c + sqrt(c * c - 4 * b * d)) / (2 * b);
    double root4 = (-c - sqrt(c * c - 4 * b * d)) / (2 * b);

    // Calculate the sum of the roots
    double sum = root1 + root2 + root3 + root4;

    // Calculate the product of the roots
    double product = root1 * root2 * root3 * root4;

    // Calculate the absolute difference between the sum and product
    double difference = abs(sum - product);

    return difference;
}