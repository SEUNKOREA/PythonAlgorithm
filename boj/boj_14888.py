"""
BOJ 14888. 연산자 끼워넣기
출처: https://www.acmicpc.net/problem/14888
"""
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, res, cnt):
    if n == N-1:
        global mx, mn
        mx = max(mx, res)
        mn = min(mn, res)
        return
    for i in range(4):
        if cnt[i] > 0:
            cnt[i] -= 1
            if i == 0:
                dfs(n + 1, res + lst[n + 1], cnt)
            elif i == 1:
                dfs(n + 1, res - lst[n + 1], cnt)
            elif i == 2:
                dfs(n + 1, res * lst[n + 1], cnt)
            elif i == 3:
                if res >= 0:
                    dfs(n + 1, res // lst[n + 1], cnt)
                else:
                    dfs(n + 1, -(-res // lst[n + 1]), cnt)
            cnt[i] += 1


N = int(input())
lst = list(map(int, input().split()))
cnt = list(map(int, input().split()))

mx = -9876543210
mn = 9876543210

dfs(0, lst[0], cnt)

print(mx)
print(mn)