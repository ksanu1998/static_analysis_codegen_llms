#include <bits/stdc++.h> 
 using namespace std ;
int countGroups(int position, int previous_sum, int length, char *num) {
    if (position == length) {
        return 1;
    }
    int count = 0;
    for (int i = 0; i < 10; i++) {
        if (num[position] == i + '0') {
            count += countGroups(position + 1, previous_sum + i, length, num);
        }
    }
    return count;
}