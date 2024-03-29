import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

def get_count(array, x):
    first = bisect_left(array, x)
    last = bisect_right(array, x)

    return last - first

count = get_count(array, x)

if count == 0:
    print(-1)
else:
    print(count)
