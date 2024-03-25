n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
answer = 1e9

def dfs(depth, idx):
    global answer

    if depth == n//2:
        a = 0
        b = 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += board[i][j]
                elif not visited[i] and not visited[j]:
                    b += board[i][j]

        answer = min(answer, abs(a-b))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(answer)