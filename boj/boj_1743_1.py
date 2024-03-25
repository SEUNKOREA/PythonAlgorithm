"""
boj 1743. 음식물피하기
https://www.acmicpc.net/problem/1743
"""

### BFS 풀이
from collections import deque

# 세로, 가로, 음식물 쓰레기 개수
n, m, k = map(int, input().split())
# 2차원 배열정보(0: 빈칸, 1: 쓰레기)
array = [[0] * (m+1) for _ in range(n+1)]
# 쓰레기 정보 입력받기
for _ in range(k):
    r, c = map(int, input().split())
    array[r][c] = 1
# 방문정보
visited = [[False] * (m+1) for _ in range(n+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    size = 0
    while q:
        cx, cy = q.popleft()
        size += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (1 <= nx <= n and 1 <= ny <= m) and not visited[nx][ny] and array[nx][ny] != 0:
                q.append([nx, ny])
                visited[nx][ny] = True
    return size

answer = 0
for x in range(1, n+1):
    for y in range(1, m+1):
        if array[x][y] != 0 and not visited[x][y]:
            size = bfs(x, y)
            answer = max(answer, size)
print(answer)