def printArr(arr, n):
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;


int main()
{
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int n = sizeof(arr) / sizeof(arr[0]);
    printArr(arr, n);
    rangeCoefficient(arr, n);
    printArr(arr, n);
    return 0;
}

/*
Output:
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
*/
