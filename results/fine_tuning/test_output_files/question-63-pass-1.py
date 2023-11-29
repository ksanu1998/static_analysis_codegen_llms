def lowerBound(array, length, value):
    if (length == 0)
        return -1;
    if (array[0] == value)
        return 0;
    if (array[length - 1] == value)
        return length - 1;
    int l = 0, r = length - 1;
    while (l < r) {
        int mid = (l + r) / 2;
        if (array[mid] < value)
            l = mid + 1;
        else
            r = mid;
    }
    if (array[l] == value)
        return l;
    if (array[r] == value)
        return r;
    return -1;


int main()
{
    int array[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int length = sizeof(array) / sizeof(array[0]);
    int value = 1;
    int ans = lowerBound(array, length, value);
    if (ans == -1)
        cout << "No such value found";
    else
        cout << "Minimum cost to make all array elements equal is "
             << (ans + 1) * 2;
    return 0;
}
