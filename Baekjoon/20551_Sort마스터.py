from bisect import bisect_left, bisect_right
import sys

n, m = map(int, sys.stdin.readline().split())

a = [int(sys.stdin.readline()) for _ in range(n)]
query = [int(sys.stdin.readline()) for _ in range(m)]

a.sort()

for i in range(m):
    q = query[i]
    first = bisect_left(a, q)
    second = bisect_right(a, q)
    num = first - second

    if num == 0:
        print(-1)
    else:
        print(first)