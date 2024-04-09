"""
SWEA 2001. 파리퇴치
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = -1
    for si in range(N-M+1):
        for sj in range(N-M+1):
            total = 0
            for i in range(si, si+M):
                for j in range(sj, sj+M):
                    total += arr[i][j]
            max_value = max(max_value, total)

    print(f"#{tc}", max_value)
