"""
BOJ 1987. 알파벳
출처: https://www.acmicpc.net/problem/1987
"""
import sys
sys.stdin = open('input.txt', 'r')

### dfs 풀이
# def dfs(ci, cj, cnt):
#     global ans
#     ans = max(ans, cnt)
#
#     for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         ni, nj = ci + di, cj + dj
#         if (0 <= ni < R and 0 <= nj < C) and v[ord(arr[ni][nj])] == 0:
#             v[ord(arr[ni][nj])] = 1
#             dfs(ni, nj, cnt+1)
#             v[ord(arr[ni][nj])] = 0
#
# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
#
# ans = 0
# v = [0] * 91
#
# v[ord(arr[0][0])] = 1
# dfs(0, 0, 1)
# print(ans)

# from collections import deque
# def bfs():
#     # q 등 필요데이터 생성
#     q = deque()
#     # v = [[[] for _ in range(C)] for _ in range(R)] # 리스트는 O(N)
#     v = [[set() for _ in range(C)] for _ in range(R)]
#     ans = 1
#
#     # q에 초기데이터(들) 삽입
#     q.append((0, 0, arr[0][0]))
#     v[0][0].add(arr[0][0])
#
#     while q:
#         ci, cj, cv = q.popleft()
#         ans = max(ans, len(cv))
#         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 4방향에 대해서
#             ni, nj = ci + di, cj + dj
#             # 범위 안 & 중복 알파벳 방지 & 중복 시퀀스 방지
#             if (0 <= ni < R and 0 <= nj < C) and arr[ni][nj] not in cv and cv+arr[ni][nj] not in v[ni][nj]:
#                 q.append((ni, nj, cv+arr[ni][nj]))
#                 v[ni][nj].add(cv+arr[ni][nj])
#     return ans
#
# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
# ans = bfs()
# print(ans)

