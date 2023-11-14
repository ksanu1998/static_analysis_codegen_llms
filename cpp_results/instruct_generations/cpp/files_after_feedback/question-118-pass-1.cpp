void findDistinctOddSum(ll n, ll k) {
    // Initialize a vector to store the distinct odd integers
    vector<ll> odds;
    // Initialize a variable to keep track of the sum
    ll sum = 0;
    // Loop through all possible odd integers
    for (ll i = 1; i <= n; i += 2) {
        // If the sum is less than N and the vector size is less than K, add the integer to the vector
        if (sum < n && odds.size() < k) {
            odds.push_back(i);
            sum += i;
        }
        // If the sum is greater than N, remove the first element from the vector and subtract its value from the sum
        else if (sum > n) {
            sum -= odds.front();
            odds.erase(odds.begin());
        }
        // If the vector size is equal to K, break the loop
        if (odds.size() == k) {
            break;
        }
    }
    // Print the vector of distinct odd integers
    for (auto odd : odds) {
        cout << odd << " ";
    }
    cout << endl;
}