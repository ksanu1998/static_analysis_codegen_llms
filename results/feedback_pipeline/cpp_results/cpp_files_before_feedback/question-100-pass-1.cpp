#include <bits/stdc++.h> 
 using namespace std ;
 int findAns ( int a , int b , int n ) {
int count = 0;
for (int i = 0; i <= n; i++)
{
    if (i % a == 0 && i % b == 0)
        count++;
}
return count;