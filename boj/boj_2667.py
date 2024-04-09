"""
BOJ 2667. 단지번호붙이기
출처: https://www.acmicpc.net/problem/2667
"""
import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global tmp
    arr[x][y] = 2 # 현재위치 방문처리
    tmp += 1
    # print(f"{(x, y)}", end=' ')
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1:
                dfs(nx, ny)

n = int(input()) # 지도의 크기
arr = [list(map(int, input())) for _ in range(n)]
# 1: 집이 있는 곳 >> 2: 집이 있는 곳 중에서 방문한 곳
# 0: 집이 없는 곳

total = 0
cnt = []
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            global tmp
            tmp = 0
            dfs(x, y)
            total += 1
            cnt.append(tmp)
print(total)
cnt.sort()
for c in cnt:
    print(c)