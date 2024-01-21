import sys

n = int(sys.stdin.readline()) # 7
power = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[-1] = 1

for i in range(n-2, -1, -1):
    temp = []
    for j in range(i+1, n):
        if power[i] > power[j]:
            temp.append(dp[j])
    if len(temp) != 0:
        dp[i] = max(temp) + 1
    else:
        dp[i] = 1

print(n-max(dp))