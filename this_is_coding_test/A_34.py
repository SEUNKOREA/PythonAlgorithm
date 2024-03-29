# 전체 병사의 수(n)
n = int(input())
# 각 병사들의 전투력 정보
power = list(map(int, input().split()))

# power[i]를 마지막 원소로 하는 가장 긴 부분 수열의 길이
dp = [1] * n

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if power[i] > power[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
