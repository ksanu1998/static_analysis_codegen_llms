MAX = 26


def compressString(s, n):
    # Create a dictionary to store the frequency of each character
    freq = {}
    for i in range(n):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    
    # Sort the dictionary by value
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Print the frequency of each character in alphabetical order
    for i in range(n):
        print(sorted_freq[i][0], end=" ")
    print()
