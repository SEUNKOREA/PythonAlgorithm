"""
BOJ 1987. 알파벳
출처: https://www.acmicpc.net/problem/1987
"""
import sys
sys.stdin = open('input.txt', 'r')

def dfs(ci, cj, cnt):
    global ans
    ans = max(ans, cnt)

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if (0 <= ni < R and 0 <= nj < C) and v[ord(arr[ni][nj])] == 0:
            v[ord(arr[ni][nj])] = 1
            dfs(ni, nj, cnt+1)
            v[ord(arr[ni][nj])] = 0

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

ans = 0
v = [0] * 91

v[ord(arr[0][0])] = 1
dfs(0, 0, 1)
print(ans)