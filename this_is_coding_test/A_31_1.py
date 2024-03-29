t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))

    graph = [[0] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[i*m+j]
            if j == 0:
                dp[i][j] = temp[i*m+j]

    answer = 0

    for y in range(m):
        for x in range(n):
            for i in [-1, 0, 1]:
                nx = x + i
                ny = y + 1

                if 0 <= nx < n and 0 <= ny < m:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y]+graph[nx][ny])

                    if ny == m-1:
                        answer = max(answer, dp[nx][ny])

    print(answer)


