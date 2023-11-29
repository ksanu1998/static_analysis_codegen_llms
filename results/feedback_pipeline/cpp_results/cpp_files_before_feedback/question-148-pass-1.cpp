#include <bits/stdc++.h> 
 using namespace std ;
 int countPairs ( int arr [ ] , int n ) {
int count = 0;
for (int i = 0; i < n; i++)
{
    for (int j = i + 1; j < n; j++)
    {
        if (arr[i] - i == arr[j] - j)
        {
            count++;
        }
    }
}
return count;
}