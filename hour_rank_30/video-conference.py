from collections import defaultdict


def solve(names):
    ans = []
    prefixes = defaultdict(int)
    uniq_names = defaultdict(int)
    for name in names:
        if uniq_names[name] > 0:
            ans.append(' '.join([name, str(uniq_names[name] + 1)]))
        uniq_names[name] += 1
        for i in range(len(name) - 1, 0, -1):
            prefix = name[:(len(name) - i)]
            if prefixes[prefix] == 0:
                ans.append(prefix)
            prefixes[prefix] += 1
    return ans

    # Write your code here
