"""
BOJ 14503 로봇청소기
https://www.acmicpc.net/problem/14503
"""
import sys
sys.stdin = open('input.txt', 'r')


### BFS 풀이
from collections import deque

def turn_left(d):
    if d == 0:
        return 3
    else:
        return d-1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
q.append((r, c))

cnt = 0

while q:
    ci, cj = q.popleft()

    if arr[ci][cj] == 0:  # 현재 칸 청소 X 라면
        arr[ci][cj] = 2   # 현재 칸 청소
        cnt += 1

    found = False
    for _ in range(4):

        d = turn_left(d)
        ni = ci + di[d]
        nj = cj + dj[d]
        if arr[ni][nj] == 0:
            q.append((ni, nj))
            found = True
            break

    if not found:
        ni = ci - di[d]
        nj = cj - dj[d]
        if arr[ni][nj] != 1:
            q.append((ni, nj))
        else:
            break

print(cnt)



### DFS 풀이
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solve(si, sj, dr):
    global ans
    if arr[si][sj] == 0:
        arr[si][sj] = 2
        ans += 1
    for i in range(4):
        dr = (dr + 3) % 4
        ni, nj = si+di[dr], sj+dj[dr]
        if arr[ni][nj] == 0:
            return solve(ni, nj, dr)
    ni, nj = si-di[dr], sj-dj[dr]
    if arr[ni][nj] != 1:
        return solve(ni, nj, dr)
    else:
        return

N, M = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
solve(si, sj, dr)
print(ans)
