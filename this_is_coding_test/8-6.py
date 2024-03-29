# 개미들의 식량창고 개수
n = int(input())
# 식량창고에 저장된 식량의 개수 정보 배열
data = list(map(int, input().split()))

dp = [0] * 1000

dp[0] = data[0]
dp[1] = data[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + data[i])

print(dp[n-1])