"""
BOJ 15654 N과 M(5)
출처: https://www.acmicpc.net/problem/15654
"""
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, alst):
    if n == M:
        ans.append(alst)
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, alst+[lst[i]])
            v[i] = 0



N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
v = [0] * N

ans = []
dfs(0, [])
for a in ans:
    print(*a)