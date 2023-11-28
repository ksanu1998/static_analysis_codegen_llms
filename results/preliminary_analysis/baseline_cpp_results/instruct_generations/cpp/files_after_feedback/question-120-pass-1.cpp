#include <bits/stdc++.h>
using namespace std;
map<int, int> insertPF(map<int, int> primeFact, int fact) {
    if (primeFact.find(fact)!= primeFact.end()) {
        primeFact[fact]++;
    } else {
        primeFact[fact] = 1;
    }
    return primeFact;
}
map<int, int> primeFactors(int n) {
    map<int, int> primeFact;
    while (n % 2 == 0) {
        primeFact = insertPF(primeFact, 2);
        n /= 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            primeFact = insertPF(primeFact, i);
            n /= i;
        }
    }
    if (n > 2) {
        primeFact = insertPF(primeFact, n);
    }
    return primeFact;
}
string perfectCube(int n) {
    map<int, int> primeFact = primeFactors(n);
    string result = "";
    for (auto it = primeFact.begin(); it!= primeFact.end(); it++) {
        int power = it->second;
        for (int i = 0; i < power; i++) {
            result += to_string(it->first) + "^" + to_string(power) + " ";
        }
    }
    return result;
}