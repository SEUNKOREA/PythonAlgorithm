# 숫자카드 게임
n, m = map(int, input().split())

for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)