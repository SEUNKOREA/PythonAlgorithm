a = input() # s
b = input()

len_a = len(a)
len_b = len(b)

dp = [[0] * (len_b+1) for _ in range(len_a+1)]

for i in range(1, len_a+1):
    dp[i][0] = i
for j in range(1, len_b+1):
    dp[0][j] = j

for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

print(dp[-1][-1])
