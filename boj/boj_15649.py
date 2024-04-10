"""
BOJ 15649 N과 M(1)
출처: https://www.acmicpc.net/problem/15649
"""
def dfs(n, lst):
    if n == M:              # 종료조건
        ans.append(lst)     # 정답처리
        return
    for j in range(1, N+1): # 선택지 하나씩 고려
        if v[j] == 0:       # 방문하지 않았다면
           v[j] = 1         # 방문처리
           dfs(n+1, lst+[j])
           v[j] = 0         # 복귀

N, M = map(int, input().split())
v = [0] * (N + 1)
ans = []

dfs(0, [])

for a in ans:
    print(*a)