from collections import defaultdict

def countTriplets(arr, r):
    pairs = defaultdict(int)
    triplets = defaultdict(int)
    sum = 0
    for i in arr:
        if triplets[i] > 0:
            sum += triplets[i] #This value completes mp3[val] triplets
        if pairs[i] > 0:
            triplets[i*r] += pairs[i] #This value is valid as 2° part of mp2[val] triplets
        pairs[i*r] += 1 #"Push-up" this value as possible triplet start

    return sum

