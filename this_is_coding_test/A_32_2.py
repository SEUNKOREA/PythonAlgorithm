n = int(input())
dp = [list(map(int, input().split()))for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] += max(left_up, up)

print(max(dp[-1]))
