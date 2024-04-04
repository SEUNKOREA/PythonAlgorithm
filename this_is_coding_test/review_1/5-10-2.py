"""
이코테 DFS/BFS 실전3. 음료수 얼려먹기
BFS 풀이
"""
from collections import deque
def bfs(x, y):
    array[x][y] = 2 # 초기 위치 방문처리
    q = deque([])
    q.append((x, y))
    while q:
        now_x, now_y = q.popleft()
        print(f"{now_x, now_y}", end=' ')
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if (0 <= next_x < n and 0 <= next_y < m) and array[next_x][next_y]==0:
                array[next_x][next_y] = 2
                q.append((next_x, next_y))



n, m = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

for x in range(n):
    for y in range(m):
        if array[x][y] == 0:
            bfs(x, y)
            print("얼음 완성")
            cnt += 1
print(cnt)

"""
4 5
00110
00011
11111
00000
"""