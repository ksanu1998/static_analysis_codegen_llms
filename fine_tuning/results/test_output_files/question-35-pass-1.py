def prefixProduct(a, n):
    a[0] = 1
    for (i = 1; i < n; i++)
        a[i] = a[i - 1] * a[i];
    for (i = n - 1; i >= 0; i--)
        a[i] = a[i] * a[i + 1];
    for (i = 0; i < n; i++)
        cout << a[i] << " ";
    return 0;


int main()
{
    int n = 5;
    int a[n];
    a[0] = 1;
    a[1] = 2;
    a[2] = 3;
    a[3] = 4;
    a[4] = 5;
    prefixProduct(a, n);
    return 0;
}
