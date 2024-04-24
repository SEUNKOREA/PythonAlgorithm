"""
BOJ 15657 N과 M(8)
출처: https://www.acmicpc.net/problem/15657
"""

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, s, alst):
    if n == M:
        ans.append(alst)
        return

    for j in range(s, N):
        dfs(n+1, j, alst+[lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = []

dfs(0, 0, [])

for a in ans:
    print(*a)