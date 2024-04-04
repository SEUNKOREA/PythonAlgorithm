"""
BOJ 2178 미로탐색
https://www.acmicpc.net/problem/2178
"""
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

init_x, init_y = 0, 0
visited[init_x][init_y] = True
q = deque([(init_x, init_y)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n and 0 <= ny < m) and array[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            array[nx][ny] = array[x][y] + 1
            q.append((nx, ny))

print(array[n-1][m-1])