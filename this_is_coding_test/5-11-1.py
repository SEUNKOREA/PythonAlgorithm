n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 하, 우, 상, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
result = 0

def dfs(x, y, result):
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        result += 1
        
        if x == n-1 and y == m-1:
            print(result)
            return True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny, result)

    return False


dfs(x, y, result)

        