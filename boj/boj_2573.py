"""
BOJ 2573. 빙산
출처: https://www.acmicpc.net/problem/2573
"""
import sys
sys.stdin = open('input.txt', 'r')

import copy
from collections import deque

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    narr[si][sj] = 0 # 현재 위치 방문처리

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if (0 <= ni < N and 0 <= nj < M) and narr[ni][nj] > 0:
                q.append((ni, nj))
                narr[ni][nj] = 0


### 입력처리
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0

### 빙산녹기 시작
while True:
    year += 1
    narr = copy.deepcopy(arr)

    ## 현재 빙산들 녹이기
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] > 0: # 현재 빙산이라면
                cnt_0 = 0
                # 현재 기준 4방향에 대해서 바다의 개수만큼 빼줌
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i+di, j+dj
                    if arr[ni][nj] == 0:
                        cnt_0 += 1
                narr[i][j] = max(0, narr[i][j]-cnt_0)

    ### 디버깅
    # print(f"{year}년 후")
    # for n in narr:
    #     print(n)

    arr = copy.deepcopy(narr)

    found = False   # 빙산이 존재하는지 체크할 변수
    cnt = 0         # 빙산덩어리 개수를 체크할 변수

    ### 녹고 남은 빙산덩어리 개수 세기
    for i in range(1, N-1):
        for j in range(1, M-1):
            if narr[i][j] > 0:
                found = True
                bfs(i, j)
                cnt += 1

    ### 디버깅
    # print(f"빙산덩어리의 개수는 {cnt}\n")

    ### 종료조건[1]: 빙산의 덩어리개수가 2개 이상인 경우
    if cnt >= 2 :
        print(year)
        break

    ### 종료조건[2]: 빙산의 덩어리 개수가 2개 이하인데 빙산이 하나도 없는경우
    if not found:
        print(0)
        break