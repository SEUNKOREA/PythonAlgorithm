"""
BOJ 15663 N과 M(9)
출처: https://www.acmicpc.net/problem/15663
"""

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, alst):
    if n == M:
        ans.append(alst)
        return
    prev = 0
    for j in range(N):
        if v[j] == 0 and prev != lst[j]:
            prev = lst[j]
            v[j] = 1
            dfs(n+1, alst+[lst[j]])
            v[j] = 0

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
v = [0] * N
ans = []

dfs(0, [])

for a in ans:
    print(*a)