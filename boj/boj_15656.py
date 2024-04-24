"""
BOJ 15656 N과 M(7)
출처: https://www.acmicpc.net/problem/15656
"""

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, alst):
    if n == M:
        ans.append(alst)
        return
    for j in range(N):
        dfs(n+1, alst+[lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = []
dfs(0, [])
for a in ans:
    print(*a)