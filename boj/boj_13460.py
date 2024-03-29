import sys
from collections import deque

input = sys.stdin.readline

# 세로(n), 가로(m)
n, m = map(int, input().split())

# 보드 모양 문자열 입력받기
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'B':
            bx, by = i, j
        elif graph[i][j] == 'R':
            rx, ry = i, j

# 상,하,좌,우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))

    visited = []
    visited.append((rx, ry, bx, by))

    count = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if count > 10:
                print(-1)
                return

            if graph[rx][ry] == 'O':
                print(count)
                return

            for i in range(4):
                nrx, nry = rx, ry
                while True:  # 벽(#)일 때까지 혹은 구멍일 때까지 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == 'O':
                        break

                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break

                if graph[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(
                            nby - by):  # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)


bfs(rx, ry, bx, by)