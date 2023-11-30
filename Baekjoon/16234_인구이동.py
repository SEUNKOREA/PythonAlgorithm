import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(n)] 

# 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    temp = [(x, y)]
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    temp.append((nx, ny))
    return temp

answer = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                union = bfs(i, j)
                
                if len(union) > 1:
                    flag = 1
                    # 해당 연합의 연합인구 계산
                    total = 0
                    for (x, y) in union:
                        total += graph[x][y]
                    # 해당 연합 인구수 분배
                    for (x, y) in union:
                        graph[x][y] = total // len(union)

    if flag == 0:
        break

    answer += 1

print(answer)