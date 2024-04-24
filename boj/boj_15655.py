"""
BOJ 15655 N과 M(6)
출처: https://www.acmicpc.net/problem/15655
"""

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, alst):
    global ans
    if n == N:
        if len(alst) == M:
            ans.append(alst)
        return

    dfs(n+1, alst+[lst[n]])
    dfs(n + 1, alst)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = []
dfs(0, [])
for a in ans:
    print(*a)