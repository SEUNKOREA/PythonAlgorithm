from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

init_x, init_y = 0, 0
graph[init_x][init_y] = 2
answer = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque([(init_x,init_y)])

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지도 안에 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            # 목적지에 도착했다면
            if nx == n-1 and ny == m-1:
                graph[nx][ny] = 2
                answer += 1
                break
            # 목적지에 도착하지 않았지만 괴물이 없는 곳이라면
            if graph[nx][ny]==1:
                q.append((nx, ny))
                graph[nx][ny] = 2
                answer += 1
                break
print("##### 이동한 경로는 #####")
for g in graph:
    print(g)
print(f"정답: {answer}")
