for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 1차원 배열 > 2차원 배열
    dp = []
    for i in range(0, n*m, m):
        dp.append(array[i:i+m])

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_down, left, left_up)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)
