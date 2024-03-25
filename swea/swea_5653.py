"""
5653. [모의 SW 역량테스트] 줄기세포배양
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
"""
from collections import deque

import sys
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split()) # 세로, 가로, 배양시간

    q = deque()

    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))
        for j in range(m):
            if array[i][j] != 0:
                q.append((0, i, j)) # 생성된 시간, 좌표

    while q:
        time, x, y = q.popleft()
        power = array[x][y]

        for i in range(4):

