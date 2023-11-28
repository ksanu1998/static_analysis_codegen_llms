#include <iostream>
using namespace std;
int get_max_splits(const string& num_string) {
    int max_splits = 0;
    for (int i = 1; i <= num_string.length(); i++) {
        if (num_string.length() % i == 0) {
            max_splits = max(max_splits, i);
        }
    }
    return max_splits;
}