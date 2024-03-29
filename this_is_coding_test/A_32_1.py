# 삼각형의 크기(n)
n = int(input())
# 정수 삼각형 배열 입력받기
array = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = array[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        up = dp[i-1][j]
        dp[i][j] = max(up_left, up) + array[i][j]

answer = max(dp[-1])
print(answer)
