from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(n):
        if temp[j] != 0:
            data.append((temp[j], 0, i, j)) # 바이러스 종류, 시간, x, y

target_s, target_x, target_y = map(int, input().split())

data.sort()
q = deque(data)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, time, x, y = q.popleft()
    if time == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time+1, nx, ny))
        
print(graph[target_x-1][target_y-1])

