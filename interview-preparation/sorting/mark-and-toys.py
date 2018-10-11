#soludtion for https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

def maximumToys(prices, k):
    count = 0
    sum = 0
    for i in sorted(prices):
        if sum + i > k:
            return count
        else:
            count += 1
            sum += i
    return sum

