"""
BOJ 13458 시험감독
https://www.acmicpc.net/problem/13458
"""

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N

for i in range(N):
    A[i] = max(0, A[i] - B)
    if A[i] != 0:
        if A[i] % C == 0:
            ans += A[i] // C
        else:
            ans += (A[i] // C + 1)


print(ans)