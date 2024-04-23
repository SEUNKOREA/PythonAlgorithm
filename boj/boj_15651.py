"""
BOJ 15651 N과 M(3)
출처: https://www.acmicpc.net/problem/15651
"""
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, lst):
    if n == M:
        answer.append(lst)
        return
    for i in range(1, N+1):
        dfs(n+1, lst+[i])

N, M = map(int, input().split())
answer = []
dfs(0, [])
for a in answer:
    print(*a)