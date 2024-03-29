n, m = map(int, input().split()) # 맵의 세로, 가로
x, y, direction = map(int, input().split()) # 캐릭터의 초기 위치와 초기 방향
array = [list(map(int, input().split())) for _ in range(n)] # 맵 정보

# 북동남서(0123)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -=1

# 방문처리를 위한 리스트
visited = [[False] * m for _ in range(n)]
# 현재위치 방문처리
visited[x][y] = True
# 캐릭터가 방문한 칸의 수
answer = 1
# 회전횟수
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == False and array[nx][ny] == 0: # 가보지 않은 칸이면서 육지라면
            x, y = nx, ny
            visited[x][y] = True
            answer += 1
            turn_time = 0
        else: # 가봤거나 바다라면
            turn_left()
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if array[nx][ny] == 1:
                break
            else:
                x, y = nx, ny
                turn_time = 0

print(answer)


