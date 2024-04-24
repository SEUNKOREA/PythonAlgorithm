"""
BOJ 15663 N과 M(10)
출처: https://www.acmicpc.net/problem/15664
"""
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, s, alst):
    if n == M:
        ans.append(alst)
        return

    prev = 0
    for j in range(s, N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n+1, j+1, alst+[lst[j]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []

dfs(0, 0, [])

for alst in ans:
    print(*alst)