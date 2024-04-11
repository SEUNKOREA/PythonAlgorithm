"""
BOJ 2468. 안전영역
출처: https://www.acmicpc.net/problem/2468
"""
import sys
sys.stdin = open('input.txt', 'r')
import copy
from collections import deque

### 런타임에러 발생 >>> BFS로 접근하자
def dfs(x, y):
    narr[x][y] = limit      # 현재의 위치방문처리
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < N and 0 <= ny < N) and narr[nx][ny] > limit:
            dfs(nx, ny)

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    narr[si][sj] = limit

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if (0 <= ni < N and 0 <= nj < N) and narr[ni][nj] > limit:
                q.append((ni, nj))
                narr[ni][nj] = limit

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for limit in range(0, 101): # limit 이하는 모두 물에 잠김 (물에 하나도 안잠길수있다고 했으므로 0부터 시작)
    cnt = 0                 # 안전영역의 개수를 셀 변수
    narr = copy.deepcopy(arr) # 매 limit마다 안전영역을 세기위해 arr 배열 복사

    # 안전영역 개수 탐색 및 카운트
    for i in range(N):
        for j in range(N):
            if narr[i][j] > limit:
                bfs(i, j)
                cnt += 1

    ans = max(ans, cnt)     # 정답업데이트

print(ans)
