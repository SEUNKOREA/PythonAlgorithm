"""
BOJ 7569. 토마토
https://www.acmicpc.net/problem/7569
"""
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

### 가로, 세로, 높이
M, N, H = map(int, input().split())
### 익은 토마토개수, 안 익은 토마토 개수
ripe, unripe = 0, 0

### 토마토가 담긴 상자의 정보 입력받기
arr = []
q = deque([])
for i in range(H):
    floor = []
    for j in range(N):
        row = list(map(int, input().split()))
        for k in range(M):
            if row[k] == 1: # 익은 토마토
                ripe += 1
                q.append((0, i, j, k))
            elif row[k] == 0: # 안익은 토마토
                unripe += 1
        floor.append(row)
    arr.append(floor)

time = 0
while q:
    t, h, x, y = q.popleft()
    if time < t:
        time = t
        ### 디버깅
        # print(f"{time}")
        # for floor in arr:
        #     for row in floor:
        #         print(row)
        #     print()


    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M:
            if arr[nh][nx][ny] == 0:
                q.append((t+1, nh, nx, ny))
                arr[nh][nx][ny] = 1
                ripe += 1
                unripe -= 1

if unripe == 0:
    if time == 0:
        print(0)
    else:
        print(time)
elif unripe > 0:
    print(-1)


