# solution for https://www.hackerrank.com/challenges/grid-challenge/problem

def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i+1] < arr[i]: return False
    else:
        return True

def gridChallenge(grid):
    rows = (isSorted(z) for z in zip(*grid))
    return ['NO','YES'][all(rows)]
    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
            grid_t = sorted(str(input().strip()))
            grid.append(grid_t)
        result = gridChallenge(grid)
        print(result)

