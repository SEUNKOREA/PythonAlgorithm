from collections import deque

n, m = map(int, input().split())
graph = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    temp = input()
    for j in range(1, m+1):
        graph[i][j] = int(temp[j-1])
    

visited = [[False] * (m+1) for _ in range(n+1)]

answer = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for ii in range(1, n+1):
    for jj in range(1, m+1):
        
        if graph[ii][jj] == 0 and not visited[ii][jj]:
            q = deque([(ii, jj)])
            while q:
                x, y = q.popleft()
                visited[x][y] = True
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 1 <= nx <= n and 1 <= ny <= m: 
                        if not visited[nx][ny] and graph[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = True

            answer += 1

print(answer)