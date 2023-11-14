#include <iostream>
int MinOfCubed(int k) {
    int n = 1, m = k;
    while (n <= m) {
        int mid = (n + m) / 2;
        if (mid * mid * mid == k)
            return 1;
        else if (mid * mid * mid < k)
            n = mid + 1;
        else
            m = mid - 1;
    }
    return m - n + 1;
}