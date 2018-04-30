# solution for https://www.hackerrank.com/challenges/two-characters/problem


# import sys

def twoCharaters(s):
    uniq = list(set(s))
    max_len = 0
    for i in range(0, len(uniq)):
        for j in range(i+1, len(uniq)):
            max_len = max(max_len, pairs_count(s, uniq[i], uniq[j]))
    return max_len


def pairs_count(string, a, b):
    res = []
    for i in string:
        if not res:
            if i == a or i == b:
                res.append(i)
        else:
            if i == res[-1]:
                return 0
            elif i == a or i == b:
                res.append(i)
    return len(res) if len(res) > 1 else 0


print(twoCharaters('uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon'))
