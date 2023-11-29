def EqualNumbers(a, n):
    if (n == 1)
        return 0;
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i];
    int avg = sum / n;
    int diff = 0;
    for (int i = 0; i < n; i++)
        diff += abs(a[i] - avg);
    cout << diff << endl;
    return 0;


int main()
{
    int a[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int n = sizeof(a) / sizeof(a[0]);
    EqualNumbers(a, n);
    return 0;
}

/*
Output:

1
*/
