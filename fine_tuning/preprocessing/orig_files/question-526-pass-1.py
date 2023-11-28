from math import floor


def jaro_distance(s1, s2):
    if (s1 == s2):
        return 1.0
    len1 = len(s1)
    len2 = len(s2)
    if (len1 == 0 or len2 == 0):
        return 0.0
    max_dist = (max(len(s1), len(s2)) // 2) - 1
    match = 0
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)
    for i in range(len1):
        for j in range(max(0, i - max_dist), min(len2, i + max_dist + 1)):
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
    if (match == 0):
        return 0.0
    t = 0
    point = 0
    for i in range(len1):
        if (hash_s1[i]):
            while (hash_s2[point] == 0):
                point += 1
            if (s1[i] != s2[point]):
                point += 1
                t += 1
            else:
                point += 1
        t /= 2
    return ((match / len1 + match / len2 + (match - t) / match) / 3.0)


def jaro_Winkler(s1, s2):
    jaro_dist = jaro_distance(s1, s2)
    if (jaro_dist > 0.7):
        prefix = 0
        for i in range(min(len(s1), len(s2))):
            if (s1[i] == s2[i]):
                prefix += 1
            else:
                break
        prefix = min(4, prefix)
        jaro_dist += 0.1 * prefix * (1 - jaro_dist)
    return jaro_dist


if __name__ == "__main__":
    s1 = "TRATE"
    s2 = "TRACE"
    print("Jaro-Winkler Similarity =", jaro_Winkler(s1, s2))
