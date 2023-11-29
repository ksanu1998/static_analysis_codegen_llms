#include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long 
 const ll max_Element = 1e6 + 5 ;
 int sum1 [ max_Element ] , sum2 [ max_Element ] , sum3 [ max_Element ] ;
void precomputation(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int product = 1;
            for (int k = i; k <= j; k++) {
                product *= arr[k];
            }
            sum1[i] += product;
            sum2[j] += product;
            sum3[i] += product;
            sum3[j] += product;
        }
    }
}