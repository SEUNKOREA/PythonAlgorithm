"""
SWEA 4835. 구간합
"""
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    sm = sum(arr[:m])
    min_value = max_value = sm

    for i in range(m, n):
        sm += arr[i]
        sm -= arr[i-m]
        min_value = min(min_value, sm)
        max_value = max(max_value, sm)

    print(f"#{tc}", max_value-min_value)