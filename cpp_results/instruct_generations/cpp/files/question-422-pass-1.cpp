#include <iostream> 
 using namespace std ;
int offeringNumber(int n, int templeHeight[]) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (templeHeight[i] > 0) {
            count++;
        }
    }
    return count;
}