n = int(input())

time, price = [], []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dp = [0] * (n+1)
max_value = 0
for i in range(n-1, -1, -1):
    finish_time = i + time[i]
    if finish_time <= n:
        dp[i] = max(price[i] + dp[finish_time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

