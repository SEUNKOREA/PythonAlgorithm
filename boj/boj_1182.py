"""
BOJ 1182 부분수열의 합
출처: https://www.acmicpc.net/problem/1182
"""

import sys
sys.stdin = open('input.txt', 'r')

# def dfs(n, sm, cnt):
#     global ans
#     # 종료조건 및 정답처리
#     if n == N:
#         if sm == S and cnt > 0:
#             ans += 1
#         return
#
#     # 하부함수 호출
#     dfs(n+1, sm+lst[n], cnt+1)  # 포함하는 경우
#     dfs(n+1, sm, cnt)           # 포함하지 않는 경우
#
# N, S = map(int, input().split())
# lst = list(map(int, input().split()))
#
# ans = 0
# dfs(0, 0, 0)
# print(ans)

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0

for length in range(1, N+1):
    sm = sum(lst[:length])
    if sm == S:
        ans += 1
    for i in range(0, N-length):
        sm -= lst[i]
        sm += lst[i+length]
        if sm == S:
            ans += 1

print(ans)