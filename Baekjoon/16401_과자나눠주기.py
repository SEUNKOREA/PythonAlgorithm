import sys

m, n = map(int, sys.stdin.readline().split())
snacks = list(map(int, sys.stdin.readline().split()))

start = 1
end = snacks[-1]

answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for snack in snacks:
        total += snack // mid

    if total >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)