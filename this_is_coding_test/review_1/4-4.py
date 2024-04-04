"""
이코테 구현 실전3. 게임개발
"""
import sys
sys.stdin = open('input.txt', 'r')
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

visited = [[0 for _ in range(m)] for _ in range(n)]
array = [list(map(int, input().split())) for _ in range(n)]

visited[x][y] = 1 # 현재위치 방문처리
answer = 1 # 방문한 위치의 개수

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_time = 0
while True:
    turn_left() # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        answer += 1
        turn_time = 0
        continue
    # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향모두 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로 이동한 칸 계산
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0: # 육지로 이동가능하면
            x, y = nx, ny # 이동
        else:
            break
        turn_time = 0

print(answer)



