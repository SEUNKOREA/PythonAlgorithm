from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

q = deque()
x, y = 0, 0
q.append((0, 0))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 미로찾기 공간을 벗어난 경우 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 괴물이 있다면 무시
        if graph[nx][ny] == 0:
            continue

        # 처음방문하는 곳일 경우에만 거리 업데이트
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[n-1][m-1])
