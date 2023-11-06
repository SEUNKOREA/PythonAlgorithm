import sys

num_a, num_b = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

minus = list(a-b)
n = len(minus)

if n == 0:
    print(n)
else:
    print(n)
    minus.sort()
    answer = ' '.join(map(str, minus))
    print(answer)