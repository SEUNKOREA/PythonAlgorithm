n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y = n-x-1, m-y-1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
visited[x][y] = True
result = 1

turn_time = 0
while True:
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == False and graph[nx][ny] == 0:
        visited[nx][ny] = True
        x, y = nx, ny
        result += 1
        turn_time = 0
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(result)