#include <bits/stdc++.h> 
 using namespace std ;
 int findLargestDivisor ( int n ) {
int i = 1;
while (i * i <= n)
{
    if (n % i == 0)
    {
        i++;
    }
    else
    {
        return n / (i - 1);
    }
}
return n / (i - 1);
}