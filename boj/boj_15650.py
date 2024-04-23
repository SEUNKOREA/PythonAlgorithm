"""
BOJ 15650 N과 M(2)
출처: https://www.acmicpc.net/problem/15650
"""

### 방법 1. n을 선택할 숫자로 정의
# def dfs(n, lst):
#     if n > N:
#         if len(lst) == M:
#             answer.append(lst)
#         return
#
#     dfs(n+1, lst+[n])
#     dfs(n+1, lst)
#
# N, M = map(int, input().split())
#
# answer = []
# dfs(1, [])
# answer.sort()
# for a in answer:
#     print(*a)

### 방법 2. n을 선택한 숫자의 개수로 정의
def dfs(n, s, lst):
    if n == M:
        answer.append(lst)
        return

    for j in range(s, N+1):
        dfs(n+1, j+1, lst+[j])

N, M = map(int, input().split())

answer = []
dfs(0, 1, [])
answer.sort()
for a in answer:
    print(*a)