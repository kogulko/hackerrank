def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] <= i + 1:
            next
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'
        for j in range(max(0, q[i] - 2),i):
              if q[j] > q[i]:
                bribes+=1
    return bribes
