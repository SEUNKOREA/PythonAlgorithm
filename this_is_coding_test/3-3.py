n, m = map(int, input().split())

answer = 0

for i in range(n):
    array = list(map(int, input().split()))
    min_value = min(array)
    answer = max(answer, min_value)

print(answer)