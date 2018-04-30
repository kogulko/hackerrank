#solution for https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# Key is to use greedy algorithm to always place the transmitter at the house furthest to the right possible to cover the range. O(n log n) solution due to the sorting at the beginning.

def hackerlandRadioTransmitters(x, k):
    x.sort()
    count = 0
    i = 0
    while i < len(x):
        count += 1
        loc = x[i] + k
        while i < n and x[i] <= loc: i += 1 #go to right as far as we cover i_orig as well.
        i -= 1 #this is where we place the transmitter
        #now go to the right of x[i] by k because transmitter at x[i] covers
        # houses to its right as well
        loc = x[i] + k
        while i < n and x[i] <= loc: i += 1
    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)
