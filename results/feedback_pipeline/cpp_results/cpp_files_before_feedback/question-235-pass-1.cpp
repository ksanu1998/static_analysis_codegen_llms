#include <bits/stdc++.h> 
 using namespace std ;
string getResult(int n) {
    string result = "Not divisible";
    for (int i = 0; i < 10; i++) {
        if (n % i == 0) {
            result = "Divisible";
            break;
        }
    }
    return result;
}