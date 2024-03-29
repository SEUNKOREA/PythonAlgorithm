from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

s, ans_x, ans_y = map(int, input().split())

data.sort()
q = deque(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus_num, sec, x, y = q.popleft()

    if sec == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                q.append((virus_num, sec+1, nx, ny))

print(graph[ans_x-1][ans_y-1])

