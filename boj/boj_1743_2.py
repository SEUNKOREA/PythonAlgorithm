"""
boj 1743. 음식물피하기
https://www.acmicpc.net/problem/1743
"""

### DFS 풀이
import sys
sys.setrecursionlimit(10**5)
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

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (1 <= nx <= n and 1 <= ny <= m) and not visited[nx][ny] and array[nx][ny] != 0:
            dfs(nx, ny)


answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if not visited[i][j] and array[i][j] != 0:
            cnt = 0
            dfs(i, j)
            answer = max(cnt, answer)
print(answer)
