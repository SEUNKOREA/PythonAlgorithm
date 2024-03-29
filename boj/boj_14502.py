"""
BOJ 14502 연구소
출처: https://www.acmicpc.net/problem/14502
"""

import copy
# import sys
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

cnt = 0 # 설치한 벽의 개수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0 # 안전영역의 최댓값

def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if array[nx][ny] == 0:
                array[nx][ny] = 2
                spread_virus(nx, ny)


def install_fence():
    ### 설치한 벽의 개수가 3개라면 바이러스 퍼트리기
    global cnt
    global array
    if cnt == 3:
        before_virus = copy.deepcopy(array) # 벽 설치 조합을 계속해서 확인해야하기 때문에 바이러스 퍼지기 전 상태 저장
        for x in range(n):
            for y in range(m):
                if array[x][y] == 2:
                    spread_virus(x, y)

        ### 안전영역 개수 세기
        safety_zone = 0
        for i in range(n):
            for j in range(m):
                if array[i][j] == 0:
                    safety_zone += 1
        global answer
        answer = max(answer, safety_zone)

        array = before_virus
        return

    ### 빈 공간에 벽 설치하기
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0: # 빈 공간이라면
                array[i][j] = 1  # 벽 설치
                cnt += 1         # 설치한 벽의 개수 하나 늘리기
                install_fence()  # 다음 벽 설치를 위해서 호출
                array[i][j] = 0  # 재귀함수 호출이 끝나면 원래 대로 복귀
                cnt -= 1         # 재귀함수 호출이 끝나면 원래 대로 복귀

install_fence()
print(answer)