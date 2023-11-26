def solution(S):
    vowels = []
    consonants = []
    for i in S:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels .append(i)
        else:
            consonants .append(i)
    Nc = len(consonants)
    Nv = len(vowels)
    M = Nc // (Nv - 1)
    ans = ""
    consonant_till = 0
    for i in vowels:
        ans += i
        temp = 0
        for j in range(consonant_till, min(Nc, consonant_till + M)):
            ans += consonants[j]
            temp += 1
        consonant_till += temp
    return ans


S = "aaaabbbcc"
print(solution(S))
