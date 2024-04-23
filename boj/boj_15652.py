"""
BOJ 15652 N과 M(4)
출처: https://www.acmicpc.net/problem/15652
"""

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, s, lst):
    if n == M:
        answer.append(lst)
        return
    for j in range(s, N+1):
        dfs(n+1, j, lst+[j])

N, M = map(int, input().split())
answer = []
dfs(0, 1, [])
for a in answer:
    print(*a)