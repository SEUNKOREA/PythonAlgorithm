"""
SWEA 2005. 파스칼의 삼각형
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 파스칼 삼각형의 크기
    arr = [[1] for _ in range(N)] # 파스칼 삼각형의 배열을 담을 리스트

    for i in range(1, N):
        for j in range(1, N):
            try:
                left = arr[i-1][j-1]
            except IndexError:
                left = 0
            try:
                right = arr[i-1][j]
            except IndexError:
                right = 0
            value = left + right
            if value != 0:
                arr[i].append(value)

    print(f"#{tc}")
    for a in arr:
        print(*a)