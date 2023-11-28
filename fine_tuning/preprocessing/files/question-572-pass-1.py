def MaxFreq(s):import collections

def MaxFreq(s):
    counter = collections.Counter(s)
    max_freq = max(counter.values())
    max_freq_chars = [c for c, f in counter.items() if f == max_freq]
    return ''.join(max_freq_chars)
