def solution(S):
    vowels = ["a", "e", "i", "o", "u"]
    min_dist = float("inf")
    for i in range(len(S) - 1):
        if S[i] in vowels and S[i + 1] in vowels:
            dist = abs(vowels.index(S[i]) - vowels.index(S[i + 1]))
            min_dist = min(min_dist, dist)
    return min_dist
