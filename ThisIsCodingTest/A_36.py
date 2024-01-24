a = input()
b = input()

### 초기 테이블 세팅
dp = [[] for _ in range(len(a)+1)]
for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i == 0:
            dp[i].append(j)
        else:
            if j == 0:
                dp[i].append(i)
            else:
                if a[i-1] == b[j-1]:
                    dp[i].append(dp[i-1][j-1])
                else:
                    dp[i].append(min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1) 
print(dp[-1][-1])