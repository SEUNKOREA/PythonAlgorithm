"""
BOJ 14303 로봇청소기
출처: https://www.acmicpc.net/problem/14503
"""

from collections import deque

# import sys
# sys.stdin = open('input.txt', 'r')

def turn_left(direction):
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    return direction

# 방의 크기
n, m = map(int, input().split())

# 로봇 청소기의 초기 위치와 방향
init_x, init_y, init_d = map(int, input().split())
# 방향 북동남서(0123)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방의 정보 입력받음
array = [list(map(int, input().split())) for _ in range(n)]

# 작동을 멈출때까지 청소하는 칸의 개수
answer = 0

def bfs():
    global answer

    # 방문해야할 좌표를 담을 큐
    q = deque()
    q.append((init_x, init_y, init_d))

    while q:
        x, y, direction = q.popleft()

        if array[x][y] == 0: # 청소되지 않은 빈칸이라면
            array[x][y] = 2 # 청소 진행 >> 청소완료 빈칸(즉, 방문처리)
            answer += 1

        # for a in array:
        #     print(a)
        # print()
        # 주변 4칸 중 청소되지 않은 빈칸이 있는지 확인한다.
        found = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 방안에 있는 경우
                if array[nx][ny] == 0: # 주변 4칸 중에 청소되지 않은 빈칸 발견
                    found = True
                    break

        # 주변 4칸 중에 청소되지 않은 빈칸 발견
        if found:
            while True:
                direction = turn_left(direction)
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < n and 0 <= ny < m:
                    if array[nx][ny] == 0:
                        q.append((nx, ny, direction))
                        break
        # 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
        else:
            # 바라보는 방향을 유지한채로 한칸 후진한 칸 계산
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 후진한 칸이 방안
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 1:
                    return
                else:
                    q.append((nx, ny, direction))
            else: # 방을 벗어난 경우
                return
bfs()
print(answer)



