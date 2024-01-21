n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

### i번째 일까지 일했을 때 얻을 수 있는 최대수익
dp = [0 for _ in range(n+1)]

for i in range(n):
    ### i번째 날에 상담을 진행했을 때, 상담이 가능한 모든 날짜가 j
    for j in range(i+schedule[i][0], n+1):
        print(f"j={j}")
        print(f"dp[j]={dp[j]}, dp[i] + schedule[i][1]={dp[i] + schedule[i][1]}")
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

    print(dp)

print(dp[-1])