#include <iostream> 
 using namespace std ;
string findMaximumNum(string str, int n, int k) {
    // Initialize the maximum number as the first number in the string
    string maxNum = str.substr(0, n);

    // Loop through all possible combinations of digits
    for (int i = 0; i < (int)str.size(); i++) {
        // Get the current digit
        char currDigit = str[i];

        // Loop through all possible digits that can be used as a replacement
        for (int j = 0; j < 10; j++) {
            // If the current digit is not the same as the replacement digit, and the number of changes made so far is less than or equal to K
            if (currDigit!= '0' && j!= currDigit - '0' && k > 0) {
                // Replace the current digit with the replacement digit in a copy of the string
                string newStr = str;
                newStr[i] = '0' + j;

                // Recursively call the function to find the maximum number that can be formed by changing at most K - 1 digits
                string maxNumRec = findMaximumNum(newStr, n, k - 1);

                // If the maximum number found by the recursive call is greater than the current maximum number, update the current maximum number
                if (maxNumRec > maxNum) {
                    maxNum = maxNumRec;
                }
            }
        }
    }

    return maxNum;
}