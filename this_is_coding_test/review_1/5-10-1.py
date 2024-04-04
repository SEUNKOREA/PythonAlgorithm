"""
이코테 DFS/BFS 실전3. 음료수 얼려먹기
DFS 풀이
"""
def dfs(x, y):
    array[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n and 0 <= ny < m) and array[nx][ny] == 0:
            dfs(nx, ny)

n, m = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for x in range(n):
    for y in range(m):
        if array[x][y] == 0:
            dfs(x, y)
            cnt += 1
print(cnt)

"""
4 5
00110
00011
11111
00000
"""