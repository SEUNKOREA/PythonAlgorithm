from itertools import permutations

def solution(n, weak, dist):
    weakSize = len(weak)
    for i in range(weakSize):
        weak.append(weak[i]+n)
    
    minCnt = int(1e9)

    for start in range(weakSize):
        startPos = start
        for d in permutations(dist, len(dist)):
            endPos = weak[startPos] + d[0]
