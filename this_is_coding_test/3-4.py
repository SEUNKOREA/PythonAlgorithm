n, m = map(int, input().split())
answer = 0
for _ in range(n):
    array = list(map(int, input().split()))
    min_value = 10001
    for elt in array:
        min_value = min(min_value, elt)
    answer = max(0, min_value)
print(answer)