from collection import defaultdict


def freqQuery(queries):
    ans = []
    counts = defaultdict(int)
    freq = defaultdict(int)
    for a, b in queries:
        if a == 1:
            freq[counts[b]] -= 1
            counts[b] += 1
            freq[counts[b]] += 1
        elif a == 2 and counts[b] > 0:
            freq[counts[b]] -= 1
            counts[b] -= 1
            freq[counts[b]] += 1
        elif a == 3:
            ans.append(1) if (freq[b] > 0) else ans.append(0)
    return ans
