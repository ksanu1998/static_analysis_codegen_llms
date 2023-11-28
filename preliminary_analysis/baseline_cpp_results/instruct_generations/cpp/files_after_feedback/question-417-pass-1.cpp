#include <stdio.h>
int getTotalNumberOfSequences(int m, int n) {
    int count = 0;
    for (int i = m; i <= n; i++) {
        count++;
    }
    return count;
}
int main() {
    int m, n;
    scanf("%d%d", &m, &n);
    int total = getTotalNumberOfSequences(m, n);
    printf("Total number of sequences: %d\n", total);
    return 0;
}